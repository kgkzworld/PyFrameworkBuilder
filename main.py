"""
.DESCRIPTION
	This library will create a folder structure for a python project.
    It will create the folders and files specified in the config.yaml file.
    It can also initialize a git repository and create a conda or virtual environment if specified.
    The default name of the project is 'project' and the default path is the current directory.

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
	o argparse # This library will provide a way to parse command line arguments
	o os # This library provides a way to work with the operating system
	o subprocess # This library will provide a way to run shell commands
	o sys # This library provides access to some variables used or maintained by the interpreter
	o libs.create_file # This library will create the files specified in the config.yaml file
	o libs.create_folder # This library will create the folders specified in the config.yaml file
	o libs.isNotebook # This library will check if the script is running in a Jupyter notebook
	o libs.load_config # This library will load the config.yaml file
	o libs.set_gitignore # This library will set the .gitignore file
	o libs.timestamp # This library will provide a timestamp for the logs and output
	o pathlib # This library will provide a way to work with file paths
	o rich # This library will provide a way to print rich text to the console

.BUILD NOTES
	o 1.0.0.20250102
		[Michael Arroyo] Initial Post

.EXAMPLES
	Command: python main.py -h
    Description: Show the help message
    Notes:
    Output:

    Command: python .\\main.py
    Description: Create a new python folder structure in the current directory
    Notes: The default name of the project is 'project' and the default path is the current directory
    Output:

    Command: python .\\main.py --path C:\\Source\\Dev\\ --name myproject
    Description: Create a new python folder structure in the specified directory with the specified name
    Notes:
    Output:

    Command: python .\\main.py --path C:\\Source\\Dev\\ --name myproject --git
    Description: Initialize a git repository in the specified directory with the specified name
    Notes:
    Output:

    Command: python .\\main.py --path C:\\Source\\Dev\\ --name myproject --git --venv_init
    Description: Initialize a git repository and create a virtual environment in the specified directory
    Notes:
    Output:

    Command: python .\\main.py --path C:\\Source\\Dev\\ --name myproject --conda
    Description: Create a conda environment in the specified directory
    Notes:
    Output:

    Command: python .\\main.py --path C:\\Source\\Dev\\ --name myproject --conda --python=3.13
    Description: Create a conda environment in the specified directory with the specified python version
    Notes: The default python version is set from the config.yaml file
    Output:

    Command: python .\\main.py --path C:\\Source\\Dev\\ --name myproject --git --conda --python=3.13
    Description: Initialize a git repository and create a conda environment in the specified directory with the specified python version
    Notes: The default python version is set from the config.yaml file
    Output:

    Command: pytest .\\tests -v
    Description: With pytest run the tests in the tests folder
    Notes: This will run all the tests in the tests folder
    Output:

    Command: pytest .\\tests -m gitpush -v
    Description: With pytest run the tests in the tests folder with the gitpush marker.
    Notes: These tests are mandatory before pushing to the repository
    Output:

    Command: pytest .\\tests -m project_only -v
    Description: With pytest run the tests in the tests folder with the project_only marker.
    Notes: These tests are developer defined tests.  Not mandatory before pushing to the repository
    Output:
"""

import argparse # This library will provide a way to parse command line arguments
import os # This library provides a way to work with the operating system
import subprocess # This library will provide a way to run shell commands
import sys # This library provides access to some variables used or maintained by the interpreter
import libs.dynamic_help # This library will provide a way to create dynamic help for the project

from libs.create_file import create_file # This library will create the files specified in the config.yaml file
from libs.create_folder import create_folder # This library will create the folders specified in the config.yaml file
from libs.isNotebook import is_notebook # This library will check if the script is running in a Jupyter notebook
from libs.load_config import load_config # This library will load the config.yaml file
from libs.new_object import new_object # This library will create a new object and return it
from libs.set_gitignore import set_gitignore # This library will set the .gitignore file
from libs.timestamp import timestamp # This library will provide a timestamp for the logs and output
from pathlib import Path # This library will provide a way to work with file paths
from rich import print # This library will provide a way to print rich text to the console

def main(current_args):
    '''Main function to create the folder structure'''
    try:
        git_init = current_args.git_init
    except AttributeError:
        git_init = False

    try:
        conda_init = current_args.conda_init
    except AttributeError:
        conda_init = False

    try:
        venv_init = current_args.venv_init
    except AttributeError:
        venv_init = False

    try:
        path = current_args.path
    except AttributeError:
        path = './'

    try:
        name = current_args.name
    except AttributeError:
        name = 'project'

    parent_dir = os.path.join(path, name)
    working_dir = Path(__file__).parent
    config = load_config(working_dir)
    conda_dir = os.path.join(parent_dir, 'conda')
    git_ignore_file = os.path.join(parent_dir, '.gitignore')

    try:
        python_version = current_args.python
    except AttributeError:
        python_version = config['general']['python_version']

    if conda_init:
        venv_init = False
    if venv_init:
        conda_init = False

    try:
        os.makedirs(parent_dir)
        os.chdir(parent_dir)
    except FileExistsError:
        print('[red][-] Folder already exists![/red]')
        sys.exit(1)

    create_folder(parent_dir, config['content']['folders'])
    create_file(parent_dir, config['content']['files'])
    set_gitignore(git_ignore_file, config['gitignore'])

    if git_init:
        cmd_git_init = 'git init'
        result = subprocess.run(cmd_git_init, shell=True, capture_output=True, text=True, check=False)
        if result.returncode != 0:
            timestamp('[red][-] Error initializing git repository![/red]', 'error')
            timestamp(result.stderr, 'error')
        else:
            print('[green][+] Git repository initialized successfully![/green]')

    if conda_init:
        cmd_conda_create = f'conda create --prefix=conda python={python_version} --yes'
        result = subprocess.run(cmd_conda_create, shell=True, capture_output=True, text=True, check=False)
        if result.returncode != 0:
            print('[red][-] Error creating conda environment![/red]')
            print(result.stderr)
        else:
            print('[green][+] Conda environment created successfully!\n[/green]')
            print('[yellow][!] To activate the environment, run the following command:[/yellow]')
            print(f'[yellow][!] conda activate {conda_dir}\n[/yellow]')

    if venv_init:
        cmd_venv_create = 'python -m venv venv'
        result = subprocess.run(cmd_venv_create, shell=True, capture_output=True, text=True, check=False)

        if result.returncode != 0:
            cmd_venv_create = 'python3 -m venv venv'
            result = subprocess.run(cmd_venv_create, shell=True, capture_output=True, text=True, check=False)

        if result.returncode != 0:
            print('[red][-] Error creating virtual environment![/red]')
            print(result.stderr)
        else:
            print('[green][+] Virtual environment created successfully!\n[/green]')
            print('[yellow][!] To activate the environment, run the following command:[/yellow]')
            print('[yellow][!] For Windows:[/yellow]')
            print('[yellow][!] venv\\Scripts\\activate\n[/yellow]')
            print('[yellow][!] For Linux/Mac:[/yellow]')
            print('[yellow][!] source venv/bin/activate\n[/yellow]')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a folder structure for a python project')
    parser.add_argument('-v', '--version', action='store_true', help='show the version of the script')
    parser.add_argument('-g', '--git_init', action='store_true', help='initialize a git repository in the current directory')
    parser.add_argument('-c', '--conda_init', action='store_true', help='create a conda environment in the current directory')
    parser.add_argument('-venv', '--venv_init', action='store_true', help='create a virtual environment in the current directory')
    parser.add_argument('-p', '--path', default='./', help='path to create the folder structure in')
    parser.add_argument('-n', '--name', default='project', help='name of the project')
    parser.add_argument('-py', '--python', help='python version to use in (conda only)')
    parser.add_argument('-exm', '--examples', action='store_true', help='example of the project to create')
    args = parser.parse_args()

    if args.examples:
        arg_obj = new_object()
        arg_obj.module = __file__
        arg_obj.examples = True

        libs.dynamic_help.main(arg_obj)
        sys.exit(0)

    if args.version:
        arg_obj = new_object()
        arg_obj.module = __file__
        arg_obj.version = True

        libs.dynamic_help.main(arg_obj)
        sys.exit(0)

    main(args)