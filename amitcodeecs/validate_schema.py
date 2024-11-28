import json
import glob
from jsonschema import validate, ValidationError

# Load the schema
with open('user_schema.json') as schema_file:
    user_schema = json.load(schema_file)

# Loop through all JSON files in the current directory
for json_file in glob.glob('*.json'):
    with open(json_file) as f:
        data = json.load(f)
        try:
            validate(instance=data, schema=user_schema)
            print(f"{json_file}: Schema validation passed.")
        except ValidationError as e:
            print(f"{json_file}: Schema validation error - {e.message}")
