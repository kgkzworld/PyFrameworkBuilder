"""
.DESCRIPTION
	This library will load the a yaml configuration file.

.NOTES
	[Original Author]
		o Michael Arroyo
	[Original Build Version]
		o 1.0.0.20250102 (Major.Minor.Patch.Date<YYYYMMDD>)
	[Latest Author]
		o Michael Arroyo
	[Latest Build Version]
		o 1.0.1.20250104 (Major.Minor.Patch.Date<YYYYMMDD>)
	[Comments]
		o
	[Python Compatibility / Tested On]
		o Python 3.13.1
	[Forked Project]
		o

.DEPENDENCIES
	o os # This library provides a way to work with the operating system
    o yaml # This library will provide a way to work with yaml files

.BUILD NOTES
	o 1.0.0.20250102
		[Michael Arroyo] Initial Post
	o 1.0.1.20250104
		[Michael Arroyo] Added the ability to load a configuration file from a specified path
		[Michael Arroyo] Removed the dual parameter option and replaced it with a single parameter option

.EXAMPLES
	Command:    from load_config import load_config
                load_config('./config/myproject.yaml')
	Description: This will load the configuration file 'myproject.yaml' from the 'config' directory
	Notes: The default file name is 'config.yaml'
	Output:
"""

import os # This library provides a way to work with the operating system
import yaml # This library will provide a way to work with yaml files

def load_config(file_path):
    '''load the configuration file'''
    with open(file_path, 'r') as f:
        config = yaml.safe_load(f)
    return config