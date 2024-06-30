from jsonschema import validate, ValidationError
import os
import json
import pytest


json_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resources', 'schemas', 'nacionality_schema.json'))
with open(json_file_path, 'r') as f:
    nacionality_schema = json.load(f)

class AssertionSchemaNationality:
    @staticmethod
    def assert_nationality_list_schema(data):
        try:
            validate(instance=data, schema=nacionality_schema)
        except ValidationError as e:
            pytest.fail(f"Response JSON does not match schema: {e.message}")
