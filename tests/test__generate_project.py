import shutil
from pathlib import Path

import pytest

from tests.utils.project import generate_project


@pytest.fixture
def setup_dir() -> Path:
    generated_repo_dir: Path = generate_project(template={"repo_name": "repo_test"})
    yield generated_repo_dir
    shutil.rmtree(path=generated_repo_dir)


def test__can_generate_project(setup_dir):
    assert setup_dir.exists()
