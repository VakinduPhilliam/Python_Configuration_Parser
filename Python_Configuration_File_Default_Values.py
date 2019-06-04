# Python Configuration File Parser
# configparser — Configuration file parser
# This module provides the ConfigParser class which implements a basic configuration language which provides a structure similar to what’s found in
# Microsoft Windows INI files. You can use this to write Python programs which can be customized by end users easily.
#
# Default values are available in both types of ConfigParsers.
# They are used in interpolation if an option used is not defined elsewhere.
# 

import configparser

# New instance with 'bar' and 'baz' defaulting to 'Life' and 'hard' each

config = configparser.ConfigParser({'bar': 'Life', 'baz': 'hard'})
config.read('example.cfg')

print(config.get('Section1', 'foo'))     # -> "Python is fun!"

config.remove_option('Section1', 'bar')
config.remove_option('Section1', 'baz')

print(config.get('Section1', 'foo'))     # -> "Life is hard!"
