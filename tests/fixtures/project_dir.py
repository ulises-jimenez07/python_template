

import json
import shutil
import subprocess
from copy import deepcopy
from pathlib import Path
from tempfile import template
from typing import Dict

import pytest

from tests.utils.project import generate_project


@pytest.fixture
def project_dir(scope="function") -> Path:
    template_values = {
        "repo_name": "test-repo"
    }
    generated_repo_dir= generate_project(template_values = template_values)
    yield generated_repo_dir
    shutil.rmtree(path=generated_repo_dir)