from libs.timestamp import timestamp
from rich import print

def set_gitignore(gitignore_file, append_list):
    with open(gitignore_file, 'a') as gf:
        for item in append_list:
            gf.write(f'{item}\n')
            timestamp(f'[green][+] Added {item} to .gitignore[/green]')