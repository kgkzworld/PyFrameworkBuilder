import os
import pytest
from pathlib import Path

@pytest.mark.gitpush
def test_requirements():
    file_path = Path(__file__).parent.parent / 'requirements.txt'
    file_info = os.stat(file_path)
    assert file_info.st_size > 0