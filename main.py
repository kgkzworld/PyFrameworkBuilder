import argparse
import os
import subprocess
import sys

from libs.create_file import create_file
from libs.create_folder import create_folder
from libs.example_help import example_help
from libs.isNotebook import is_notebook
from libs.load_config import load_config
from libs.set_gitignore import set_gitignore
from libs.timestamp import timestamp
from pathlib import Path
from rich import print

def main(current_args):
    '''Main function to create the folder structure'''
    git_init = current_args.git_init
    conda_init = current_args.conda_init
    venv_init = current_args.venv_init
    path = current_args.path
    name = current_args.name
    parent_dir = os.path.join(path, name)
    working_dir = Path(__file__).parent
    conda_dir = os.path.join(parent_dir, 'conda')
    git_ignore_file = os.path.join(parent_dir, '.gitignore')
    python_version = current_args.python

    if conda_init:
        venv_init = False
    if venv_init:
        conda_init = False

    config = load_config(working_dir)

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
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('-g', '--git_init', action='store_true', help='initialize a git repository in the current directory')
    parser.add_argument('-c', '--conda_init', action='store_true', help='create a conda environment in the current directory')
    parser.add_argument('-venv', '--venv_init', action='store_true', help='create a virtual environment in the current directory')
    parser.add_argument('-p', '--path', default='./', help='path to create the folder structure in')
    parser.add_argument('-n', '--name', default='project', help='name of the project')
    parser.add_argument('-py', '--python', help='python version to use in (conda only)')
    parser.add_argument('-exm', '--examples', action='store_true', help='example of the project to create')
    args = parser.parse_args()

    if args.examples:
        example_help()
        sys.exit(1)

    main(args)