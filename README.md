## VIM PLUGINS PROFILER

[vim-plugins-profiler](https://github.com/bulletmark/vim-plugins-profiler)
is a small utility which outputs a sorted list of [vim
editor](http://www.vim.org) plugin startup times in millisec. Only vim
plugins you have installed personally in your home directory are
considered. This utility was written for Linux platforms but should work
on other platforms as well, including Mac and Windows.

The latest version and documentation is available at
https://github.com/bulletmark/vim-plugins-profiler.

### USAGE

Just run at command line, e.g.:
```
$ vim-plugins-profiler
   1:    16.759 (54.4%) nerdtree
   2:     4.248 (13.8%) vim-airline
   3:     2.880 ( 9.3%) delimitMate
   4:     2.000 ( 6.5%) tabular
   5:     1.596 ( 5.2%) emmet-vim
   6:     1.579 ( 5.1%) YouCompleteMe
   7:     0.668 ( 2.2%) ctrlp.vim
   8:     0.399 ( 1.3%) vim-surround
   9:     0.271 ( 0.9%) vim-better-whitespace
  10:     0.155 ( 0.5%) vim-commentary
  11:     0.141 ( 0.5%) autoload_cscope.vim
  12:     0.080 ( 0.3%) ag.vim
  13:     0.034 ( 0.1%) vim-javascript
  14:     0.015 ( 0.0%) typescript-vim
  15:     0.010 ( 0.0%) vim-vue
```

- The plugin startup times are in millisec, sorted from highest usage to
  lowest.
- The percentages are the percent of total plugin startup time
  (i.e. the total plugin time additional to normal vim startup time)
  that each plugin contributes.

#### OPTIONAL ARGUMENTS

```
usage: vim-plugins-profiler [-h] [-e EXE] [-r RUNS] [-n NUM]

Output sorted summary of VIM plugin startup times in millisecs.

optional arguments:
  -h, --help            show this help message and exit
  -e EXE, --exe EXE     vim executable name or path, default="vim"
  -r RUNS, --runs RUNS  number of sample runs to average over, default=4
  -n NUM, --num NUM     limit output to given number of plugins
```

### INSTALLATION

NOTE: Arch Linux users can just install
[vim-plugins-profiler from the AUR](https://aur.archlinux.org/packages/vim-plugins-profiler/).

Requires python 3.5 or later. Note [vim-plugins-profiler is on
PyPI](https://pypi.org/project/vim-plugins-profiler) so you can
`sudo pip3 install vim-plugins-profiler` or:

```
git clone https://github.com/bulletmark/vim-plugins-profiler
cd vim-plugins-profiler
# Requires python3-pip package installed:
sudo pip3 install .
```

There is no configuration required.

### UPGRADE

```
cd vim-plugins-profiler  # Source dir, as above
git pull
sudo pip3 install -U .
```

### REMOVAL

```
sudo pip3 uninstall vim-plugins-profiler
```

### LICENSE

Copyright (C) 2018 Mark Blakeney. This program is distributed under the
terms of the GNU General Public License. This program is free software:
you can redistribute it and/or modify it under the terms of the GNU
General Public License as published by the Free Software Foundation,
either version 3 of the License, or any later version.
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
Public License at <https://www.gnu.org/licenses/> for more details.
