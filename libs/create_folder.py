"""
.DESCRIPTION
	This library will create a folder in the specified directory.

.NOTES
	[Original Author]
		o Michael Arroyo
	[Original Build Version]
		o 1.0.0.20250102 (Major.Minor.Patch.Date<YYYYMMDD>)
	[Latest Author]
		o Michael Arroyo
	[Latest Build Version]
		o 1.0.0.20250102 (Major.Minor.Patch.Date<YYYYMMDD>)
	[Comments]
		o
	[Python Compatibility / Tested On]
		o Python 3.13.1
	[Forked Project]
		o

.DEPENDENCIES
	o import os # This library provides a way to work with the operating system
    o timestamp # This library will provide a timestamp for the logs and output
    o rich # This library will provide a way to print rich text to the console

.BUILD NOTES
	o 1.0.0.20250102
		[Michael Arroyo] Initial Post

.EXAMPLES
	Command: create_folder('./', 'New_Test_Folder')
	Description: This will create a folder called 'New_Test_Folder' in the current directory
	Notes:
	Output: [green][+] Folder New_Test_Folder created successfully![/green]
"""

import os

from libs.timestamp import timestamp
from rich import print

def create_folder(parent_dir, folders):
    '''create the folders'''
    try:
        for folder in folders:
            os.makedirs(os.path.join(parent_dir, folder))
            timestamp(f'[green]Folder {folder} created successfully![/green]', 'alert')
    except Exception as e:
        timestamp(f'[red][-] Error creating folder {folder}![/red]', 'error')
        timestamp(e, 'error')