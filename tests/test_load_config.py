import os
import pytest
import sys

from pathlib import Path

libs_path = Path(__file__).parent.parent / 'libs'
project_path = Path(__file__).parent.parent
parent_path = Path(__file__).parent
sys.path.insert(0, str(libs_path))
config_file_path = os.path.join(project_path, 'config.yaml')

import load_config

@pytest.mark.project_only
def test_config_exists():
    file_info = os.stat(config_file_path)
    assert file_info.st_size > 0

@pytest.mark.project_only
def test_load_config():
    assert load_config.load_config(project_path) is not None