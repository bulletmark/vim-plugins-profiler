## VIM PLUGINS PROFILER

[vim-plugin-profiler](https://github.com/bulletmark/vim-plugin-profiler)
is a small utility which outputs a sorted list of [vim
editor](http://www.vim.org) plugin startup times in millisec. Only vim
plugins you have installed personally in your home directory are
considered. This utility was written for Linux platforms but should work
on other platforms as well, including Mac and Windows.

The latest version and documentation is available at
https://github.com/bulletmark/vim-plugins-profiler.

### USAGE

Just run at command line, e.g.:
~~~~
$ vim-plugins-profiler
   1:    17.423 (72.1%) nerdtree
   2:     2.131 ( 8.8%) tabular
   3:     1.683 ( 7.0%) YouCompleteMe
   4:     1.624 ( 6.7%) emmet-vim
   5:     0.569 ( 2.4%) ctrlp.vim
   6:     0.295 ( 1.2%) vim-better-whitespace
   7:     0.156 ( 0.6%) vim-commentary
   8:     0.148 ( 0.6%) autoload_cscope.vim
   9:     0.078 ( 0.3%) ag.vim
  10:     0.035 ( 0.1%) vim-javascript
  11:     0.015 ( 0.1%) typescript-vim
  12:     0.010 ( 0.0%) vim-vue
~~~~

- The plugin startup times are in millisec, sorted from highest usage to
  lowest.
- The percentages are the percent of total plugin startup time
  (i.e. the total plugin time additional to normal vim startup time)
  that each plugin contributes.

#### OPTIONAL ARGUMENTS

~~~~
usage: vim-plugins-profiler [-h] [-n NUM]

Output sorted summary of VIM plugin startup times in millisecs.

optional arguments:
  -h, --help         show this help message and exit
  -e EXE, --exe EXE  vim executable name, default="vim"
  -n NUM, --num NUM  limit output to given number of plugins
~~~~


### INSTALLATION

NOTE: Arch Linux users can just install
[_vim-plugins-profiler from the AUR_](https://aur.archlinux.org/packages/vim-plugins-profiler/) and skip to the next section.

Requires python 3.5 or later. Type the following to install.

    git clone https://github.com/bulletmark/vim-plugins-profiler
    cd vim-plugins-profiler
    sudo make install

There is no configuration required.

### UPGRADE

    cd vim-plugins-profiler  # Source dir, as above
    git pull
    sudo make install

### REMOVAL

    sudo vim-plugin-profiler-setup uninstall

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
