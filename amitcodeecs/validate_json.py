import json
import glob

# Loop through all JSON files in the current directory
for json_file in glob.glob('*.json'):
    with open(json_file) as f:
        try:
            json.load(f)
            print(f"{json_file}: Valid JSON")
        except json.JSONDecodeError as e:
            print(f"{json_file}: Invalid JSON - {e}")
