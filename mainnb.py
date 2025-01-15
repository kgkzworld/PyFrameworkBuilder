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

    Command: python .\\main.py --list_templates
    Description: List the available templates in the templates folder
    Notes:
    Output:

    Command: python .\\main.py --use_template --path C:\\Source\\scratch\\ --git_init
    Description: Create a new python folder structure in the specified directory using the default template
    Notes:  The default template is set in the yaml configuration file.
            The default configuration file is .\\configs\\default.yaml
    Output:

    Command: python .\\main.py --use_template --template_name cybereng\v1 --path C:\\Source\\scratch\\ --git_init --venv_init
    Description: Create a new python folder structure in the specified directory using the specified template
    Notes: The default name of the project is 'project' and the default path is the current directory
    Output:

    Command: python .\\main.py --path C:\\Source\\Dev\\ --name myproject --config_file .\\SecEng.yaml
    Description: Specify the configuration file to use for the project creation
    Notes:
    Output:
"""

import marimo

__generated_with = "0.10.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo # This library will provide a way to create and manage a notebook
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    # Render an image from a URL
    mo.image(
        src="./docs/img/banner.png",
        alt="Banner",
        width=1000,
        height=600,
        rounded=True,
        caption="",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ```text
        .DESCRIPTION
        	This library will create a folder structure for a python project.
            It will create the folders and files specified in the config.yaml file.
            It can also initialize a git repository and create a conda or virtual environment if specified.
            The default name of the project is 'project' and the default path is the current directory.

        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ```text
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

        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ```text
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
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ```text
        .BUILD NOTES
        	o 1.0.0.20250102
        		[Michael Arroyo] Initial Post
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ```text
        .EXAMPLES
        	Command: python main.py --help
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

            Command: python .\main.py --list_templates
            Description: List the available templates in the templates folder
            Notes:
            Output:

            Command: python .\\main.py --use_template --path C:\\Source\\scratch\\ --git_init
            Description: Create a new python folder structure in the specified directory using the default template
            Notes:  The default template is set in the yaml configuration file.
                    The default configuration file is .\\configs\\default.yaml
            Output:

            Command: python .\main.py --use_template --template_name cybereng\v1 --path C:\\Source\\scratch\\ --git_init --venv_init
            Description: Create a new python folder structure in the specified directory using the specified template
            Notes: The default name of the project is 'project' and the default path is the current directory
            Output:

            Command: python .\\main.py --path C:\\Source\\Dev\\ --name myproject --config_file .\\SecEng.yaml
            Description: Specify the configuration file to use for the project creation
            Notes:
            Output:
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ```text
        |   .gitignore
        |   License
        |   main.py
        |   mainnb.py
        |   pytest.ini
        |   README.md
        |   requirements.txt
        |
        +---classes
        |       .gitkeep
        |       __init__.py
        |
        +---configs
        |       default.yaml
        |
        +---docs
        |   |   .gitkeep
        |   |
        |   \---img
        |           banner.png
        |
        +---libs
        |   |   .gitkeep
        |   |   create_file.py
        |   |   create_folder.py
        |   |   dynamic_help.py
        |   |   isNotebook.py
        |   |   load_config.py
        |   |   new_object.py
        |   |   set_gitignore.py
        |   |   timestamp.py
        |   |   __init__.py
        |
        +---logs
        |       .gitkeep
        |
        +---notebooks
        |   |   .gitkeep
        |   |   mermaid_graph.ipynb
        |   |
        |
        +---templates
        |   \---cybereng
        |       \---v1
        |           |   .gitignore
        |           |   License
        |           |   main.py
        |           |   pytest.ini
        |           |   README.md
        |           |   requirements.txt
        |           |
        |           +---classes
        |           |       .gitkeep
        |           |       __init__.py
        |           |
        |           +---docs
        |           |       .gitkeep
        |           |
        |           +---libs
        |           |   |   .gitkeep
        |           |   |   create_file.py
        |           |   |   create_folder.py
        |           |   |   dynamic_help.py
        |           |   |   isNotebook.py
        |           |   |   load_config.py
        |           |   |   new_object.py
        |           |   |   set_gitignore.py
        |           |   |   timestamp.py
        |           |   |   __init__.py
        |           |
        |           +---logs
        |           |       .gitkeep
        |           |
        |           +---notebooks
        |           |       .gitkeep
        |           |       __init__.py
        |           |
        |           +---tests
        |           |   |   .gitkeep
        |           |   |   test_create_file.py
        |           |   |   test_create_folder.py
        |           |   |   test_docstring_parser.py
        |           |   |   test_docstring_parser.yaml
        |           |   |   test_load_config.py
        |           |   |   test_main.py
        |           |   |   test_requirements.py
        |           |   |   test_set_gitignore.py
        |           |   |   test_structure.py
        |           |   |   test_structure.yaml
        |           |   |   __init__.py
        |
        +---tests
        |   |   .gitkeep
        |   |   test_create_file.py
        |   |   test_create_folder.py
        |   |   test_docstring_parser.py
        |   |   test_docstring_parser.yaml
        |   |   test_load_config.py
        |   |   test_main.py
        |   |   test_requirements.py
        |   |   test_set_gitignore.py
        |   |   test_structure.py
        |   |   test_structure.yaml
        |   |   __init__.py
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### **Import External Libraries**""")
    return


@app.cell
def _():
    import os # This library provides a way to work with the operating system
    import subprocess # This library will provide a way to run shell commands
    import sys # This library provides access to some variables used or maintained by the interpreter
    import typer
    import libs.dynamic_help # This library will provide a way to create dynamic help for the project

    from contextlib import redirect_stdout # This library will provide a way to redirect the standard output
    from dirsync import sync # This library will provide a way to sync directories
    from io import StringIO # This library will provide a way to work with string inputs and outputs
    from libs.create_file import create_file # This library will create the files specified in the config.yaml file
    from libs.create_folder import create_folder # This library will create the folders specified in the config.yaml file
    from libs.load_config import load_config # This library will load the config.yaml file
    from libs.new_object import new_object # This library will create a new object and return it
    from libs.set_gitignore import set_gitignore # This library will set the .gitignore file
    from libs.timestamp import timestamp # This library will provide a timestamp for the logs and output
    from pathlib import Path # This library will provide a way to work with file paths
    from rich import print # This library will provide a way to print rich text to the console
    return (
        Path,
        StringIO,
        create_file,
        create_folder,
        libs,
        load_config,
        new_object,
        os,
        print,
        redirect_stdout,
        set_gitignore,
        subprocess,
        sync,
        sys,
        timestamp,
        typer,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### **Set Project Variables**""")
    return


@app.cell
def _(Path, __file__, mo):
    parent_dir = mo.notebook_dir()
    working_dir = Path(__file__).parent
    template_dir = Path(__file__).parent / 'templates'
    return parent_dir, template_dir, working_dir


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### **Set Parameter default values**

        * Print Marimo Arguments if this project is running in a Notebook.<br>
        * Update any of the default values with values found from the arguments in the CLI
        """
    )
    return


@app.cell
def _(Path, __file__, mo, print):
    valid_parameters = {
        "name": "project",
        "path": "./",
        "config_file": Path(__file__).parent / 'configs' / 'default.yaml',
        "venv_init": False,
        "conda_init": False,
        "git_init": False,
        "use_template": False,
        "list_templates": False,
        "python_version": None,
        "template_name": None,
        "debug": False,
        "notebook": False,
        "autorun": False
    }

    if mo.running_in_notebook():
        print(mo.cli_args().get('debug'))
        print(mo.cli_args().get_all)

        if mo.cli_args():
            for valid_arg in mo.cli_args():
                if mo.cli_args().get(valid_arg) == '':
                    valid_parameters[valid_arg] = True
                else:
                    valid_parameters[valid_arg] = mo.cli_args().get(valid_arg)

        if valid_parameters['debug']:
            print(valid_parameters)
    return valid_arg, valid_parameters


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### **Function: list the templates in the template folder**

        * This function is only available from the CLI (**not the notebook**)
        """
    )
    return


@app.cell
def _(os, print):
    def list_templates(start_dir):
        '''
        .DESCRIPTION
            This function will list the templates in the templates folder

        .PARAMETERS
            start_dir: str
        '''
        template_list = []
        for root, dirs, files in os.walk(start_dir):
            # Calculate the depth by counting the slashes in the path
            relative_path = os.path.relpath(root, start_dir)
            depth = relative_path.count(os.sep)

            # Only print paths up to 2 levels deep
            if depth == 1:
                template_list.append(relative_path)
                continue

        print("\n[bold yellow] Available templates:[/bold yellow]")
        print("[bold yellow] ********************[/bold yellow]")
        if len(template_list) == 0:
            print('[red][-] No templates found![/red]')
        else:
            for template in template_list:
                print(f'[green][+] {template}[/green]')
        print("")
    return (list_templates,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### **Function: print all argument values**""")
    return


@app.cell
def _(print):
    def print_args(args):
        print("\n")
        print(f'name: {args.name}')
        print(f'path: {args.path}')
        print(f'config_file: {args.config_file}')
        print(f'venv_init: {args.venv_init}')
        print(f'conda_init: {args.conda_init}')
        print(f'git_init: {args.git_init}')
        print(f'use_template: {args.use_template}')
        print(f'list_templates: {args.list_templates}')
        print(f'python_version: {args.python_version}')
        print(f'template_name: {args.template_name}')
        print(f'debug: {args.debug}')
        print(f'notebook: {args.notebook}')
        print(f'autorun: {args.autorun}')
        print("\n")
    return (print_args,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### **Function: Determine if the parent directory already exists**""")
    return


@app.cell
def _(os, sys, timestamp):
    def check_main_dir(args):
        try:
            os.makedirs(args.project_dir)
            os.chdir(args.project_dir)
        except FileExistsError:
            timestamp('[red]Folder already exists![/red]', 'error')
            sys.exit(1)
    return (check_main_dir,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### **Function: Build the project folder and files**""")
    return


@app.cell
def _(
    StringIO,
    create_file,
    create_folder,
    print,
    redirect_stdout,
    set_gitignore,
    sync,
    sys,
    timestamp,
):
    def build_project(args):
        if args.use_template:
            try:
                with StringIO() as f, redirect_stdout(f):
                    sync(args.template_name, args.project_dir, 'sync')
                timestamp('[green]Template copied successfully![/green]', 'alert')
            except Exception as e:
                timestamp('[red]Error copying template![/red]', 'error')
                print(e)
                sys.exit(1)
        else:
            create_folder(args.project_dir, args.config['content']['folders'])
            create_file(args.project_dir, args.config['content']['files'])
            set_gitignore(args.git_ignore_file, args.config['gitignore'])
    return (build_project,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""### **Function: Initialize Git Structure**""")
    return


@app.cell
def _(print, print_args, subprocess, timestamp):
    def build_git_init(args):
        cmd_git_init = 'git init'

        if args.debug:
            print(f"Git Command Line: {cmd_git_init}")
            print_args(args)

        result = subprocess.run(cmd_git_init, shell=True, capture_output=True, text=True, check=False)
        if result.returncode != 0:
            timestamp('[red]Error initializing git repository![/red]', 'error')
            timestamp(result.stderr, 'error')
        else:
            timestamp('[green]Git repository initialized successfully![/green]', 'alert')
    return (build_git_init,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### **Function: Initialize Virtual Environment**""")
    return


@app.cell
def _(print, subprocess, timestamp):
    def build_venv_init(args):
        cmd_venv_create = 'python -m venv venv'

        if args.debug:
            print(f"venv Command Line: {cmd_venv_create}")

        result = subprocess.run(cmd_venv_create, shell=True, capture_output=True, text=True, check=False)

        if result.returncode != 0:
            cmd_venv_create = 'python3 -m venv venv'
            result = subprocess.run(cmd_venv_create, shell=True, capture_output=True, text=True, check=False)

        if result.returncode != 0:
            timestamp('[red]Error creating virtual environment![/red]', 'error')
            timestamp(result.stderr, 'error')
        else:
            timestamp('[green]Virtual environment created successfully!\n[/green]', 'alert')
            timestamp('[yellow]To activate the environment, run the following command:[/yellow]', 'warning')
            timestamp('[yellow]For Windows:[/yellow]', 'warning')
            timestamp('[yellow]venv\\Scripts\\activate\n[/yellow]', 'warning')
            timestamp('[yellow]For Linux/Mac:[/yellow]', 'warning')
            timestamp('[yellow]source venv/bin/activate\n[/yellow]', 'warning')
    return (build_venv_init,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### **Function: Initialize Conda Environment**""")
    return


@app.cell
def _(print, print_args, subprocess, timestamp):
    def build_conda_init(args):
        cmd_conda_create = f'conda create --prefix=conda python={args.python_version} --yes'

        if args.debug:
            print(f"Conda Command Line: {cmd_conda_create}")
            print_args(args)

        result = subprocess.run(cmd_conda_create, shell=True, capture_output=True, text=True, check=False)
        if result.returncode != 0:
            timestamp('[red]Error creating conda environment![/red]', 'error')
            timestamp(result.stderr, 'error')
        else:
            timestamp('[green]Conda environment created successfully!\n[/green]', 'alert')
            timestamp('[yellow][!] To activate the environment, run the following command:[/yellow]', 'warning')
            timestamp(f'[yellow][!] conda activate {args.conda_dir}\n[/yellow]', 'warning')
    return (build_conda_init,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### **Function: Main**
        ```text
        1) Update Args values   
        2) Print Args if running debug
        3) Process the Build values
            o check_main_dir
            o build_project
            o build_git_init
            o build_venv_init
            o build_conda_init
        ```
        """
    )
    return


@app.cell
def _(
    Path,
    __file__,
    build_conda_init,
    build_git_init,
    build_project,
    build_venv_init,
    check_main_dir,
    load_config,
    os,
    print,
    timestamp,
):
    def main(args):

        args.project_dir = os.path.join(args.path, args.name)
        args.working_dir = Path(__file__).parent
        args.config = load_config(args.config_file)
        args.conda_dir = os.path.join(args.project_dir, 'conda')
        args.git_ignore_file = os.path.join(args.project_dir, '.gitignore')
        args.template_dir = Path(__file__).parent / 'templates'

        if args.python_version == None:
            args.python_version = args.config['general']['python_version']

        if args.template_name == None:
            args.template_name = args.config['template']['default']

        if args.conda_init:
            args.venv_init = False
        if args.venv_init:
            args.conda_init = False

        if args.debug:
            print(f'name = {args.name}')
            print(f'path = {args.path}')
            print(f'config_file = {args.config_file}')
            print(f'venv_init = {args.venv_init}')
            print(f'conda_init = {args.conda_init}')
            print(f'git_init = {args.git_init}')
            print(f'project_dir = {args.project_dir}')
            print(f'working_dir = {args.working_dir}')
            print(f'config = {args.config}')
            print(f'conda_dir = {args.conda_dir}')
            print(f'git_ignore_file = {args.git_ignore_file}')
            print(f'template_dir = {args.template_dir}')
            print(f'use_template = {args.use_template}')
            print(f'list_templates = {args.list_templates}')
            print(f'python_version = {args.python_version}')
            print(f'template_name = {args.template_name}')
            print(f'debug = {args.debug}')
            print(f'autorun = {args.autorun}')
            print(f'notebook = {args.notebook}')

        if args.debug == False:
            check_main_dir(args)
            build_project(args)

            if args.git_init:
                build_git_init(args)

            if args.venv_init:
                build_venv_init(args)

            if args.conda_init:
                build_conda_init(args)

        timestamp(f'[green]Created project: {args.name} in {args.path}![/green]', 'alert')
    return (main,)


@app.cell
def _(mo):
    mo.md(
        r"""
        ### **Pause:  If you're running this process in a notebook, the process is halted unless you run the --autorun flag.**
        If you want to continue running the full process in this notebook, click on the "Run (Cell run_notebook)" button.
        """
    )
    return


@app.cell
def _(mo):
    run_notebook = mo.ui.run_button(label="Run (Cell run_notebook)")
    run_notebook
    return (run_notebook,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### **Notebook Processing**

        This cell will not run by default while in a notebook.  To execute this cell you either need to click on the above Run Notebook button or use the --autorun parameter in the CLI
        """
    )
    return


@app.cell
def _(main, mo, new_object, print_args, run_notebook, valid_parameters):
    #Cell run_notebook
    if mo.running_in_notebook():
        # if mo.cli_args():
        #     for arg in mo.cli_args():
        #         if mo.cli_args().get(arg) == '':
        #             valid_parameters[arg] = True
        #         else:
        #             valid_parameters[arg] = mo.cli_args().get(arg)

        new_args = new_object()
        new_args.name = valid_parameters['name']
        new_args.path = valid_parameters['path']
        new_args.config_file = valid_parameters['config_file']
        new_args.venv_init = valid_parameters['venv_init']
        new_args.conda_init = valid_parameters['conda_init']
        new_args.git_init = valid_parameters['git_init']
        new_args.use_template = valid_parameters['use_template']
        new_args.list_templates = valid_parameters['list_templates']
        new_args.python_version = valid_parameters['python_version']
        new_args.template_name = valid_parameters['template_name']
        new_args.debug = valid_parameters['debug']
        new_args.notebook = valid_parameters['notebook']
        new_args.autorun = valid_parameters['autorun']

        if new_args.debug:
            print_args(new_args)

        if new_args.autorun == False:
            mo.stop(not run_notebook.value, "Click the 'Run (Cell run_notebook)' to continue")

        main(new_args)
    return (new_args,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### **Typer Function:**

        This is the function that manages all actions via the CLI.  

        * Function: **Create** - The (Create) command is used to build the new Python environment
        * Function: **Template** - The (Template) command will allow you to build a new Python environment from a template
        """
    )
    return


@app.cell
def _(
    main,
    mo,
    new_object,
    print,
    print_args,
    subprocess,
    sys,
    typer,
    valid_parameters,
):
    mo.stop(mo.running_in_notebook())
    from typing_extensions import Annotated

    app = typer.Typer()

    @app.command()
    def create(
        name: Annotated[str, typer.Option("--name", "-n", help="Type in the Project name")] = valid_parameters['name'],
        path: Annotated[str, typer.Option("--path", "-p", help="Type in the Project path")] = valid_parameters['path'],
        config_file: Annotated[str, typer.Option("--config_file", "-c", help="Type in the Config file path")] = valid_parameters['config_file'],
        venv_init: Annotated[bool, typer.Option("--venv_init", "-vi", help="Enable venv environment")] = valid_parameters['venv_init'],
        conda_init: Annotated[bool, typer.Option("--conda_init", "-ci", help="Enable conda environment")] = valid_parameters['conda_init'],
        git_init: Annotated[bool, typer.Option("--git_init", "-gi", help="Enable git environment")] = valid_parameters['git_init'],
        use_template: Annotated[bool, typer.Option("--use_templates", "-ut", help="Show a complete list of templates")] = valid_parameters['use_template'],
        list_templates: Annotated[bool, typer.Option("--list_templates", "-lt", help="Show a complete list of templates")] = valid_parameters['list_templates'],
        python_version: Annotated[str, typer.Option("--python_version", "-pv", help="Specify the Python Version to use.  The default is set in the config file")] = valid_parameters['python_version'],
        template_name: Annotated[str, typer.Option("--template_name", "-tn", help="Specify the template name to copy.  The default is set in the config file")] = valid_parameters['template_name'],
        debug: Annotated[bool, typer.Option("--debug", "-d", help="Debug values in Notebook")] = valid_parameters['debug'],
        notebook: Annotated[bool, typer.Option("--notebook", "-nb", help="Run Notebook")] = valid_parameters['notebook'],
        autorun: Annotated[bool, typer.Option("--autorun", "-a", help="AutoRun Notebook Cells on Notebook startup")] = valid_parameters['autorun']

    ):
        new_args = new_object()
        new_args.name = name
        new_args.path = path
        new_args.config_file = config_file
        new_args.venv_init = venv_init
        new_args.conda_init = conda_init
        new_args.git_init = git_init
        new_args.use_template = use_template
        new_args.list_templates = list_templates
        new_args.python_version = python_version
        new_args.template_name = template_name
        new_args.debug = debug
        new_args.notebook = notebook
        new_args.autorun = autorun

        if new_args.debug:
                print_args(new_args)

        if new_args.notebook:
            cmd_notebook = 'marimo edit mainnb.py --'

            for arg in new_args.__dict__:
                if new_args.__dict__[arg] != None:
                    if new_args.__dict__[arg] == True:
                        cmd_notebook += f' --{arg} True'
                    elif new_args.__dict__[arg] == False:
                        cmd_notebook += f' --{arg} False'
                    else:
                        cmd_notebook += f' --{arg} {new_args.__dict__[arg]}'

            if new_args.debug:
                print(f'cmd_notebook = {cmd_notebook}')

            result = subprocess.run(cmd_notebook, shell=True, check=False)
            sys.exit(0)

        main(new_args)

    app()
    return Annotated, app, create


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
