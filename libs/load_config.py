import os
import yaml

def load_config(path):
    '''load the configuration file'''
    yaml_file = os.path.join(path, 'config.yaml')
    with open(yaml_file, 'r') as f:
        config = yaml.safe_load(f)
    return config