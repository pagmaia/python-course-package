import subprocess
from pathlib import Path


def test__linting_passes(setup_dir: Path):
    subprocess.run(["make", "lint-ci"], cwd=setup_dir, check=True)


def test__tests_pass(setup_dir: Path):
    subprocess.run(["make", "install"], cwd=setup_dir, check=True)
    subprocess.run(["make", "test-wheel-locally"], cwd=setup_dir, check=True)
