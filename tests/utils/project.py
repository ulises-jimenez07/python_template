import json
import subprocess
from copy import deepcopy
from typing import Dict

from tests.consts import PROJECT_DIR


def generate_project(template_values: Dict[str, str]):
    template_values = deepcopy(template_values)
    cookiecutter_config = {
        "default_context" : {"repo_name": "test-repo"} 
    }
    cookiecutter_config_fpath = PROJECT_DIR / "cookiecutter-test-config.json"
    cookiecutter_config_fpath.write_text(json.dumps(cookiecutter_config))

    cmd = [
        "cookiecutter",
        str(PROJECT_DIR),
        "--output-dir",
        str( PROJECT_DIR /"sample"),
        "--no-input",
        "--config-file",
        str(cookiecutter_config_fpath)
    ]
    print("COMMAND: ", " ".join(cmd))
    subprocess.run(cmd, check=True )
    generated_repo_dir = PROJECT_DIR / "sample" / cookiecutter_config["default_context"]["repo_name"]
    return generated_repo_dir
