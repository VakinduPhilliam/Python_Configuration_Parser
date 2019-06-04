# Python Configuration File Parser
# configparser — Configuration file parser
# This module provides the ConfigParser class which implements a basic configuration language which provides a structure similar to what’s found in
# Microsoft Windows INI files. You can use this to write Python programs which can be customized by end users easily.
#
# NOTE:
# config parsers don’t support escaping of comment prefixes so using inline_comment_prefixes may prevent users from specifying option values with characters
# used as comment prefixes. When in doubt, avoid setting inline_comment_prefixes.
#
# In any circumstances, the only way of storing comment prefix characters at the beginning of a line in multiline values is to interpolate the prefix,
# for example:
# 

from configparser import ConfigParser, ExtendedInterpolation

parser = ConfigParser(interpolation=ExtendedInterpolation())

# the default BasicInterpolation could be used as well

parser.read_string("""
    [DEFAULT]
    hash = #

    [hashes]
    shebang =
      ${hash}!/usr/bin/env python
      ${hash} -*- coding: utf-8 -*-

    extensions =
      enabled_extension
      another_extension
      #disabled_by_comment
      yet_another_extension

    interpolation not necessary = if # is not at line start
    even in multiline values = line #1
      line #2
      line #3
    """)

print(parser['hashes']['shebang'])

#!/usr/bin/env python
# -*- coding: utf-8 -*-

print(parser['hashes']['extensions'])

#
# OUTPUT:
#
# enabled_extension
# another_extension
# yet_another_extension

print(parser['hashes']['interpolation not necessary'])

if # is not at line start

print(parser['hashes']['even in multiline values'])

#
# OUTPUT:
#
# line #1
# line #2
# line #3
