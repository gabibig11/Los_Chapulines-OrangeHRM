from __future__ import annotations

import json
from pathlib import Path

BASE = Path(__file__).absolute().parent.parent


def resources_schemas_path(path):
    return BASE / "resources" / "schemas"/ path


def load_schema_resource(filename):
    with resources_schemas_path(filename).open() as f:
        return json.load(f)