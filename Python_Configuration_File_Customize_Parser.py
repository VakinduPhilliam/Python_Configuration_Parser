# Python Configuration File Parser
# configparser — Configuration file parser
# This module provides the ConfigParser class which implements a basic configuration language which provides a structure similar to what’s found in
# Microsoft Windows INI files. You can use this to write Python programs which can be customized by end users easily.
#
# Customizing Parser Behaviour
# There are nearly as many INI format variants as there are applications using it. configparser goes a long way to provide support for the largest sensible
# set of INI styles available.
# The default functionality is mainly dictated by historical background and it’s very likely that you will want to customize some of the features.
#
# Please note: there are ways to add a set of key-value pairs in a single operation. When you use a regular dictionary in those operations, the order of the
# keys may be random.
#
# For example:
# 

parser = configparser.ConfigParser()

parser.read_dict({'section1': {'key1': 'value1',
                                   'key2': 'value2',
                                   'key3': 'value3'},
                      'section2': {'keyA': 'valueA',
                                   'keyB': 'valueB',
                                   'keyC': 'valueC'},
                      'section3': {'foo': 'x',
                                   'bar': 'y',
                                   'baz': 'z'}
    })

parser.sections()  

# OUTPUT: '['section3', 'section2', 'section1']'

[option for option in parser['section3']] 

# OUTPUT: '['baz', 'foo', 'bar']'

# 
# In these operations you need to use an ordered dictionary as well:
# 

from collections import OrderedDict

parser = configparser.ConfigParser()

parser.read_dict(
      OrderedDict((
        ('s1',
         OrderedDict((
           ('1', '2'),
           ('3', '4'),
           ('5', '6'),
         ))
        ),
        ('s2',
         OrderedDict((
           ('a', 'b'),
           ('c', 'd'),
           ('e', 'f'),
         ))
        ),
      ))
    )

parser.sections()  

# OUTPUT: '['s1', 's2']'

[option for option in parser['s1']]  

# OUTPUT: '['1', '3', '5']'

[option for option in parser['s2'].values()]  

# OUTPUT: '['b', 'd', 'f']'
 
# > allow_no_value, default value: False
#
# Some configuration files are known to include settings without values, but which otherwise conform to the syntax supported by configparser.
# The allow_no_value parameter to the constructor can be used to indicate that such values should be accepted:
# 

import configparser

sample_config = """
     [mysqld]
      user = mysql
      pid-file = /var/run/mysqld/mysqld.pid
      skip-external-locking
      old_passwords = 1
      skip-bdb
      # we don't need ACID today
      skip-innodb
    """

config = configparser.ConfigParser(allow_no_value=True)
config.read_string(sample_config)

# Settings with values are treated as before:

config["mysqld"]["user"]

# OUTPUT: 'mysql'

# Settings without values provide None:

config["mysqld"]["skip-bdb"]

# Settings which aren't specified still raise an error:

config["mysqld"]["does-not-exist"]
