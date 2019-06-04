# Python Configuration File Parser
# configparser — Configuration file parser
# This module provides the ConfigParser class which implements a basic configuration language which provides a structure similar to what’s found in
# Microsoft Windows INI files. You can use this to write Python programs which can be customized by end users easily.
#
# read(filenames, encoding=None). 
# Attempt to read and parse an iterable of filenames, returning a list of filenames which were successfully parsed.
# If filenames is a string, a bytes object or a path-like object, it is treated as a single filename. If a file named in filenames cannot be opened, that
# file will be ignored. This is designed so that you can specify an iterable of potential configuration file locations (for example, the current directory, 
# the user’s home directory, and some system-wide directory), and all existing configuration files in the iterable will be read.
# If none of the named files exist, the ConfigParser instance will contain an empty dataset. An application which requires initial values to be loaded from
# a file should load the required file or files using read_file() before calling read() for any optional files:
# 

import configparser, os

config = configparser.ConfigParser()
config.read_file(open('defaults.cfg'))

config.read(['site.cfg', os.path.expanduser('~/.myapp.cfg')],
            encoding='cp1250')
