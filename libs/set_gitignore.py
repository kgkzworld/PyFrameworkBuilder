"""
.DESCRIPTION
	This library will set the .gitignore files contents with the specified list

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
	o timestamp # This library will provide a timestamp for the logs and output
    o rich # This library will provide a way to print rich text to the console

.BUILD NOTES
	o 1.0.0.20250102
		[Michael Arroyo] Initial Post

.EXAMPLES
	Command:    from set_gitignore import set_gitignore
                set_gitignore('.gitignore', ['*.log'])
	Description: This will add '*.log' to the .gitignore file
	Notes:
	Output:

    Command:    from set_gitignore import set_gitignore
                set_gitignore('/source/dev/.gitignore', update_list)
    Description: This will add the contents of the update_list to the .gitignore file
    Notes:
    Output:
"""

from libs.timestamp import timestamp # This library will provide a timestamp for the logs and output
from rich import print # This library will provide a way to print rich text to the console

def set_gitignore(gitignore_file, append_list):
    '''this function will set the .gitignore file with the specified list'''
    with open(gitignore_file, 'a') as gf:
        for item in append_list:
            gf.write(f'{item}\n')
            timestamp(f'[green][+] Added {item} to .gitignore[/green]')