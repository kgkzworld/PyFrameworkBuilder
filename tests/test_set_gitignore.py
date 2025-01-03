import os
import pytest
from pathlib import Path

@pytest.mark.gitpush
def test_gitignore():
    file_path = Path(__file__).parent.parent / '.gitignore'
    file_info = os.stat(file_path)
    assert file_info.st_size > 0