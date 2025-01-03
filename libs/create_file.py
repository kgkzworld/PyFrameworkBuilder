"""
.DESCRIPTION
	This library will create a file in the specified directory.

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
	Command: create_file('./', 'new_file.txt')
	Description: This will create a new file called new_file.txt in the current directory.
	Notes:
	Output: [green][+] File new_file.txt created successfully![/green]
"""
import os # This library provides a way to work with the operating system

from libs.timestamp import timestamp # This library will provide a timestamp for the logs and output
from rich import print # This library will provide a way to print rich text to the console

def create_file(parent_dir, files):
    '''create the files'''
    try:
        for file in files:
            with open(os.path.join(parent_dir, file), 'w') as f:
                pass
            timestamp(f'[green][+] File {file} created successfully![/green]', 'alert')
    except Exception as e:
        timestamp(f'[red][-] Error creating file {file}![/red]', 'error')
        timestamp(e, 'error')