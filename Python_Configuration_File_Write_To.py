# Python Configuration File Parser
# configparser — Configuration file parser
# This module provides the ConfigParser class which implements a basic configuration language which provides a structure similar to what’s found in
# Microsoft Windows INI files. You can use this to write Python programs which can be customized by end users easily.
#
# Mainly because of backwards compatibility concerns, configparser provides also a legacy API with explicit get/set methods.
# While there are valid use cases for the methods outlined below, mapping protocol access is preferred for new projects.
# The legacy API is at times more advanced, low-level and downright counterintuitive.
# 
# An example of writing to a configuration file:
# 

import configparser

config = configparser.RawConfigParser()

# Please note that using RawConfigParser's set functions, you can assign
# non-string values to keys internally, but will receive an error when
# attempting to write to a file or when you get it in non-raw mode. Setting
# values using the mapping protocol or ConfigParser's set() does not allow
# such assignments to take place.

config.add_section('Section1')
config.set('Section1', 'an_int', '15')

config.set('Section1', 'a_bool', 'true')
config.set('Section1', 'a_float', '3.1415')
config.set('Section1', 'baz', 'fun')

config.set('Section1', 'bar', 'Python')
config.set('Section1', 'foo', '%(bar)s is %(baz)s!')

# Writing our configuration file to 'example.cfg'

with open('example.cfg', 'w') as configfile:
    config.write(configfile)
