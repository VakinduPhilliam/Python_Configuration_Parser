# Python Configuration File Parser
# configparser — Configuration file parser
# This module provides the ConfigParser class which implements a basic configuration language which provides a structure similar to what’s found in
# Microsoft Windows INI files. You can use this to write Python programs which can be customized by end users easily.
#
# Reading Configuration File
# After creating a configuration file, then comes, reading a configuration file and exploring the data it holds.
# The API is pretty straightforward. 
 
config = configparser.ConfigParser()
config.sections()

# OUTPUT: '[]'

config.read('example.ini')

# OUTPUT: '['example.ini']'

config.sections()

# OUTPUT: '['bitbucket.org', 'topsecret.server.com']'

'bitbucket.org' in config

# OUTPUT: 'True'

'bytebong.com' in config

# OUTPUT: 'False'

config['bitbucket.org']['User']

# OUTPUT: 'hg'

config['DEFAULT']['Compression']

# OUTPUT: 'yes'

topsecret = config['topsecret.server.com']
topsecret['ForwardX11']

# OUTPUT: 'no'

topsecret['Port']

# OUTPUT: '50022'

for key in config['bitbucket.org']:  
        print(key)

# OUTPUT: 'yes'
 