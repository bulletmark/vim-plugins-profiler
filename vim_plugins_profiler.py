#!/usr/bin/env python3
'Output sorted summary of VIM plugin startup times in millisecs.'
# Mark Blakeney, Jan 2018
import os
import sys
import argparse
import subprocess
import tempfile
import statistics
from pathlib import Path
from collections import defaultdict

HOME = Path.home()

# Set of subdirs to exclude
EXCLUDED = {'autoload', 'colors', 'compiler', 'doc', 'ftplugin', 'indent',
        'keymap', 'lang', 'macros', 'pack', 'print', 'spell', 'syntax',
        'tools', 'tutor', 'ftdetect', 'after', '.config', 'site'}

def remove_common(paths):
    'Remove any common path prefix from given dict of paths'
    if not paths:
        return paths

    prefix = os.path.commonpath(paths)
    return {Path(p).relative_to(prefix): v for p, v in paths.items()}

def whittle_down(paths):
    'Whittle down paths by removing excluded dirs and common prefixes'
    while True:
        pathscopy = paths.copy()
        paths = {p: v for p, v in paths.items() if
                len(p.parts) > 1 and p.parts[0] not in EXCLUDED}
        paths = remove_common(paths)
        if paths == pathscopy:
            break

    return paths

def do_sample_run(prog, tmpfile, logfile):
    notaterm = '' if any(p in prog for p in ('nvim', 'neovim')) \
            else ' --not-a-term'

    'Run editor and capture a sample of plugin times'
    cmd = f'{prog} -Xf -V0{notaterm} --startuptime {logfile.name} '\
            f'-cqa {tmpfile.name}'
    try:
        res = subprocess.run(cmd.split(), universal_newlines=True,
                             stdout=subprocess.DEVNULL)
    except Exception as e:
        sys.exit(e)

    if res.returncode != 0:
        sys.exit(f'.. exited with {prog} error.')

    # Create dict of paths and times
    paths = defaultdict(float)
    for line in logfile:
        if ': sourcing /' not in line:
            continue

        junk, junk, tstr, junk, fname = line.split()

        # Only concerned with personal plugins
        try:
            fpath = Path(fname).relative_to(HOME)
        except ValueError:
            continue

        paths[fpath] += float(tstr.rstrip(':'))

    # Now remove any common path prefix and excluded dirs
    paths = whittle_down(remove_common(paths))

    # Now assume plugin name is unique top dir name and so tally times.
    times = defaultdict(float)
    for path, val in paths.items():
        times[path.parts[0]] += val

    # Return times for each plugin, for this run
    return times

def main():
    opt = argparse.ArgumentParser(description=__doc__.strip())
    opt.add_argument('-e', '--exe', default='vim',
            help='vim executable name or path, default="%(default)s"')
    opt.add_argument('-r', '--runs', type=int, default=4,
            help='number of sample runs to average over, default=%(default)d')
    opt.add_argument('-n', '--num', type=int,
            help='limit output to given number of plugins')
    args = opt.parse_args()

    'Do N sample runs and accumulate times for each plugin in a list'
    plugins = defaultdict(list)
    diffs = None
    for run in range(args.runs):

        # For each run we need an empty file to edit, and a log file
        with tempfile.NamedTemporaryFile('r') as tmpfile, \
                tempfile.NamedTemporaryFile('r') as logfile:
            times = do_sample_run(args.exe, tmpfile, logfile)

        # Do sanity check to ensure we have consistent set of
        # plugins found each sample run
        names = set(times)
        if not plugins:
            plugin_names = names
        elif plugin_names != names:
            diffs = plugin_names.symmetric_difference(names)
            diffstr = ', '.join(str(i) for i in diffs)
            print(f'{len(diffs)} inconsistent plugins found in sample run '
                    f'{run + 1}:\n{diffstr}', file=sys.stderr)
            continue

        # Add new sample run times to list for each plugin
        for plugin, val in times.items():
            plugins[plugin].append(val)

    # Calculate a representative time from each plugins list of sample times
    times = {p: statistics.median(v) for p, v in plugins.items()}

    # Output sorted results
    if times and not diffs:
        percent = 100. / sum(times.values())
        for ind, plugin in enumerate(sorted(times, key=times.get,
                reverse=True), 1):
            if args.num and ind > args.num:
                break

            v = times[plugin]
            print(f'{ind:4}: {v:9.3f} ({v * percent:4.1f}%) {plugin}')

if __name__ == '__main__':
    sys.exit(main())
