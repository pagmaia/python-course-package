import json
import subprocess
from copy import deepcopy
from pathlib import Path
from typing import Dict

from ..consts import PROJECT_DIR


def init_git_repo(repo: Path):
    subprocess.run(["git", "init"], cwd=repo, check=True)
    subprocess.run(["git", "branch", "-M", "main"], cwd=repo, check=True)
    subprocess.run(["git", "add", "--all"], cwd=repo, check=True)
    subprocess.run(["git", "commit", "-m", "'initial commit by pytest'"])


def generate_project(template: Dict[str, str], test_session_id: str):
    template_values = deepcopy(template)
    cookiecutter_config = {"default_context": template_values}

    cookiecutter_config_fpath = PROJECT_DIR / f"tests/cookiecutter-{test_session_id}.json"
    cookiecutter_config_fpath.write_text(json.dumps(cookiecutter_config))

    subprocess.run(
        [
            "cookiecutter",
            str(PROJECT_DIR),
            "--output-dir",
            str(PROJECT_DIR / "sample"),
            "--no-input",
            "--config-file",
            str(cookiecutter_config_fpath),
        ],
        check=True,
    )
    return PROJECT_DIR / "sample" / template_values["repo_name"]
