from rich import print

def example_help():
    print("""EXAMPLES:

Example:
    Command: [green]python main.py -h[/green]
    Description: [yellow]Show the help message[/yellow]
    Notes:
    Output:

Example:
    Command: [green]python .\\main.py[/green]
    Description: [yellow]Create a new python folder structure in the current directory[/yellow]
    Notes: The default name of the project is 'project' and the default path is the current directory
    Output:

Example:
    Command: [green]python .\\main.py --path C:\\Source\\Dev\\ --name myproject[/green]
    Description: [yellow]Create a new python folder structure in the specified directory with the specified name[/yellow]
    Notes:
    Output:

Example:
    Command: [green]python .\\main.py --path C:\\Source\\Dev\\ --name myproject --git[/green]
    Description: [yellow]Initialize a git repository in the specified directory with the specified name[/yellow]
    Notes:
    Output:

Example:
    Command: [green]python .\\main.py --path C:\\Source\\Dev\\ --name myproject --git --venv_init[/green]
    Description: [yellow]Initialize a git repository and create a virtual environment in the specified directory[/yellow]
    Notes:
    Output:

Example:
    Command: [green]python .\\main.py --path C:\\Source\\Dev\\ --name myproject --conda[/green]
    Description: [yellow]Create a conda environment in the specified directory[/yellow]
    Notes:
    Output:

Example:
    Command: [green]python .\\main.py --path C:\\Source\\Dev\\ --name myproject --conda --python=3.13[/green]
    Description: [yellow]Create a conda environment in the specified directory with the specified python version[/yellow]
    Notes: The default python version is set from the config.yaml file
    Output:

Example:
    Command: [green]python .\\main.py --path C:\\Source\\Dev\\ --name myproject --git --conda --python=3.13[/green]
    Description: [yellow]Initialize a git repository and create a conda environment in the specified directory with the specified python version[/yellow]
    Notes: The default python version is set from the config.yaml file
    Output:

Example:
    Command: [green]pytest .\\tests -v[/green]
    Description: [yellow]With pytest run the tests in the tests folder[/yellow]
    Notes: This will run all the tests in the tests folder
    Output:

Example:
    Command: [green]pytest .\\tests -m gitpush -v[/green]
    Description: [yellow]With pytest run the tests in the tests folder with the gitpush marker.[/yellow]
    Notes: These tests are mandatory before pushing to the repository
    Output:

Example:
    Command: [green]pytest .\\tests -m project_only -v[/green]
    Description: [yellow]With pytest run the tests in the tests folder with the project_only marker.[/yellow]
    Notes: These tests are developer defined tests.  Not mandatory before pushing to the repository
    Output:
            """)