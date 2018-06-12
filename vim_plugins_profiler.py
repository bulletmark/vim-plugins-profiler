#!/usr/bin/env python3
'Output sorted summary of VIM plugin startup times in millisecs.'
# Mark Blakeney, Jan 2018
import os, sys, argparse, subprocess, tempfile, statistics
from pathlib import Path
from collections import defaultdict

HOME = Path.home()

# Set of subdirs to exclude
EXCLUDED = {'autoload', 'colors', 'compiler', 'doc', 'ftplugin', 'indent',
        'keymap', 'lang', 'pack', 'print', 'spell', 'syntax', 'tutor'}

opt = argparse.ArgumentParser(description=__doc__.strip())
opt.add_argument('-e', '--exe', default='vim',
        help='vim executable name or path, default="%(default)s"')
opt.add_argument('-r', '--runs', type=int, default=4,
        help='number of sample runs to average over, default=%(default)d')
opt.add_argument('-n', '--num', type=int,
        help='limit output to given number of plugins')
args = opt.parse_args()

# Need file to log to and an empty file to edit
logfile = tempfile.NamedTemporaryFile('r')
tmpfile = tempfile.NamedTemporaryFile('r')
cmd = '{} -Xf --startuptime {} -cqa {}'.format(args.exe, logfile.name,
        tmpfile.name)

def remove_common(paths):
    'Remove any common path prefix from given dict of paths'
    prefix = os.path.commonpath(paths)
    return {Path(p).relative_to(prefix): v for p, v in paths.items()}

def do_sample_run():
    'Run editor and capture a sample of plugin times'
    try:
        res = subprocess.run(cmd.split())
    except Exception as e:
        sys.exit(e)

    if res.returncode != 0:
        sys.exit('.. exited with {} error.'.format(args.exe))

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
    paths = remove_common(paths)
    paths = {p: v for p, v in paths.items() if
            len(p.parts) > 1 and p.parts[0] not in EXCLUDED}
    paths = remove_common(paths)

    # Now assume plugin name is unique top dir name and so tally times.
    times = defaultdict(float)
    for path, val in paths.items():
        times[path.parts[0]] += val

    # Return times for each plugin, for this run
    return times

def main():
    'Do N sample runs and accumulate times for each plugin in a list'
    plugins = defaultdict(list)
    for run in range(args.runs):
        times = do_sample_run()

        # Do sanity check to ensure we have consistent set of plugins found
        # each sample run
        if not plugins:
            plugin_names = set(times)
        elif plugin_names != set(times):
            sys.exit('Inconsistency in plugins found each sample run')

        # Add new sample run times to list for each plugin
        for plugin, val in times.items():
            plugins[plugin].append(val)

    # Calculate a representative time from each plugins list of sample times
    times = {p: statistics.median(v) for p, v in plugins.items()}

    # Output sorted results
    if times:
        percent = 100. / sum(times.values())
        for ind, plugin in enumerate(sorted(times, key=times.get,
                reverse=True), 1):
            if args.num and ind > args.num:
                break

            v = times[plugin]
            print('{:4}: {:9.3f} ({:4.1f}%) {}'.format(ind, v, v * percent,
                plugin))

if __name__ == '__main__':
    sys.exit(main())
