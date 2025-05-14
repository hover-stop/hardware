import os
import sys
import yaml # PyYAML

try:
    from jsonschema import validate
    from jsonschema.exceptions import ValidationError
except ImportError:
    print("Error: jsonschema library not found. Please install it by running: pip install jsonschema")
    sys.exit(1)

# Schema definition for metadata.yaml files
METADATA_SCHEMA = {
    "type": "object",
    "properties": {
        "part_number": {"type": "string", "pattern": "^\\d{5}$"},
        "owner": {"type": "string", "minLength": 1},
        "name": {"type": "string", "minLength": 1},
        "description": {"type": "string", "minLength": 1},
        "parent_assembly": {"type": "string", "pattern": "^(\\d{5}|None)$"},
        "status": {"type": "string", "enum": ["Draft", "Review", "Release", "Prototype", "Obsolete", "In Development"]},
        "part_type": {"type": "string", "enum": ["3D Printed", "Machined", "Off The Shelf", "Sheet Metal", "Electronics", "Cable or Wire", "Assembly", "Ghost", "None", "Other"]},
        "alternatives": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "description": {"type": "string", "minLength": 1},
                    "source": {"type": "string", "minLength": 1}
                },
                "required": ["description", "source"],
                "additionalProperties": False
            }
        },
        "primary_source": {"type": "string"},
        "secondary_source": {"type": "string"},
        "cost": {"type": ["string", "number"]},
        "quantity": {"type": "integer", "minimum": 1},
        "contributors": {
            "type": "array",
            "items": {"type": "string", "minLength": 1},
            "minItems": 1
        }
    },
    "required": [
        "part_number", "owner", "name", "description", "parent_assembly",
        "status", "part_type", "primary_source", "secondary_source", "cost",
        "quantity", "contributors"
    ],
    "additionalProperties": False
}

def get_project_root():
    """Determines the project root directory (assumed to be parent of 'utils')."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(script_dir)

def find_metadata_files(project_root):
    """Finds all metadata.yaml files in part directories."""
    metadata_files = []
    try:
        for item in os.listdir(project_root):
            item_path = os.path.join(project_root, item)
            if os.path.isdir(item_path) and item.isdigit() and len(item) == 5:
                metadata_path = os.path.join(item_path, 'metadata.yaml')
                if os.path.isfile(metadata_path):
                    metadata_files.append(metadata_path)
    except FileNotFoundError:
        print(f"Error: Project root directory not found at {project_root}")
        sys.exit(1)
    except Exception as e:
        print(f"Error scanning for metadata files: {e}")
        sys.exit(1)
    return metadata_files

def validate_metadata_file(file_path, schema):
    """Validates a single metadata.yaml file against the schema."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return [f"YAML parsing error: {e}"]
    except Exception as e:
        return [f"Error reading file: {e}"]

    if data is None: # Handle empty YAML file case
        return ["File is empty or not valid YAML."]

    errors = []
    try:
        validate(instance=data, schema=schema)
        # Check if part_number in file matches the directory name
        dir_name = os.path.basename(os.path.dirname(file_path))
        if str(data.get('part_number')) != dir_name:
            errors.append(f"Part number '{data.get('part_number')}' in file does not match directory name '{dir_name}'.")
    except ValidationError as e:
        # Construct a more user-friendly error message
        error_path = " -> ".join(map(str, e.path)) if e.path else "Top-level"
        errors.append(f"Schema validation error at '{error_path}': {e.message}")
    except Exception as e: # Catch any other unexpected errors during validation
        errors.append(f"Unexpected validation error: {e}")
        
    return errors

def main():
    print("Metadata Validator Utility")
    print("--------------------------")

    project_root = get_project_root()
    metadata_files = find_metadata_files(project_root)

    if not metadata_files:
        print("No metadata.yaml files found in part directories.")
        return

    print(f"Found {len(metadata_files)} metadata.yaml files. Validating...")
    total_errors = 0
    files_with_errors = 0

    for mf_path in sorted(metadata_files):
        relative_path = os.path.relpath(mf_path, project_root)
        print(f"\nValidating: {relative_path}")
        errors = validate_metadata_file(mf_path, METADATA_SCHEMA)
        if errors:
            files_with_errors += 1
            for error in errors:
                print(f"  ERROR: {error}")
                total_errors += 1
        else:
            print("  SUCCESS: Validation passed.")

    print("\n--- Validation Summary ---")
    if files_with_errors == 0:
        print(f"All {len(metadata_files)} files validated successfully!")
    else:
        print(f"{files_with_errors} file(s) out of {len(metadata_files)} had validation errors.")
        print(f"Total errors found: {total_errors}")
    print("------------------------")

if __name__ == "__main__":
    main()
