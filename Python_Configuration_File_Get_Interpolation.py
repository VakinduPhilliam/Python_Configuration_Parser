# Python Configuration File Parser
# configparser — Configuration file parser
# This module provides the ConfigParser class which implements a basic configuration language which provides a structure similar to what’s found in
# Microsoft Windows INI files. You can use this to write Python programs which can be customized by end users easily.
#
# To get interpolation, use ConfigParser:
# 

import configparser

cfg = configparser.ConfigParser()
cfg.read('example.cfg')

# Set the optional *raw* argument of get() to True if you wish to disable
# interpolation in a single get operation.

print(cfg.get('Section1', 'foo', raw=False))  # -> "Python is fun!"
print(cfg.get('Section1', 'foo', raw=True))   # -> "%(bar)s is %(baz)s!"

# The optional *vars* argument is a dict with members that will take
# precedence in interpolation.

print(cfg.get('Section1', 'foo', vars={'bar': 'Documentation',
                                       'baz': 'evil'}))

# The optional *fallback* argument can be used to provide a fallback value

print(cfg.get('Section1', 'foo'))

      # -> "Python is fun!"

print(cfg.get('Section1', 'foo', fallback='Monty is not.'))

      # -> "Python is fun!"

print(cfg.get('Section1', 'monster', fallback='No such things as monsters.'))

      # -> "No such things as monsters."

# A bare print(cfg.get('Section1', 'monster')) would raise NoOptionError
# but we can also use:

print(cfg.get('Section1', 'monster', fallback=None))

      # -> None
