import os
import sys
import datetime
import random # Added import for random number generation
# Ensure PyYAML is installed: pip install PyYAML
try:
    import yaml
except ImportError:
    print("Error: PyYAML library not found. Please install it by running: pip install PyYAML")
    sys.exit(1)

def get_project_root():
    """Determines the project root directory (assumed to be parent of 'utils')."""
    script_dir = os.path.dirname(os.path.abspath(__file__)) 
    return os.path.dirname(script_dir)

def get_existing_part_numbers(project_root):
    """Scans the project root for existing 5-digit part number directories."""
    existing_parts = set()
    try:
        for item in os.listdir(project_root):
            item_path = os.path.join(project_root, item)
            if os.path.isdir(item_path) and item.isdigit() and len(item) == 5:
                existing_parts.add(int(item))
    except FileNotFoundError:
        print(f"Error: Project root directory not found at {project_root}")
        sys.exit(1)
    except Exception as e:
        print(f"Error scanning for existing part numbers: {e}")
        sys.exit(1)
    return existing_parts

def generate_unique_part_number(existing_part_numbers):
    """Generates a unique random 5-digit part number."""
    # Attempt to find a unique random number a reasonable number of times
    # (90000 possible 5-digit numbers from 10000-99999)
    # Max attempts can be adjusted if needed.
    max_attempts = 1000 
    for _ in range(max_attempts):
        num = random.randint(10000, 99999)
        if num not in existing_part_numbers:
            return num
    print(f"Error: Could not find an available unique random 5-digit part number after {max_attempts} attempts.")
    print("This might indicate a very high number of existing parts or an unlikely series of random collisions.")
    sys.exit(1)

def prompt_for_metadata(part_number_str):
    """Prompts the user for part metadata."""
    print("\nPlease enter the following metadata for the new part:")
    
    owner_input = input("Owner (e.g., Kurisu): ").strip()
    name = input(f"Part Name (e.g., Main Body, Bracket - do not include part number '{part_number_str}'): ").strip()
    description = input("Description: ").strip()
    parent_assembly = input("Parent Assembly (e.g., 31000, or 'None'): ").strip() or "None"
    status = input("Status (e.g., Draft, Prototype, Released) [Draft]: ").strip() or "Draft"
    part_type = input("Part Type (e.g., 3D Printed, Machined, COTS) [3D Printed]: ").strip() or "3D Printed"
    
    print("\nAlternatives (enter one per line, blank line to finish):")
    alternatives_list = []
    while True:
        alt_desc = input("  Alternative Description (or blank to finish): ").strip()
        if not alt_desc:
            break
        alt_source = input(f"  Source for '{alt_desc}' [To be determined]: ").strip() or "To be determined"
        alternatives_list.append({'description': alt_desc, 'source': alt_source})
        
    primary_source = input("Primary Source (e.g., In-house prototype, Vendor XYZ): ").strip()
    secondary_source = input("Secondary Source (or 'None yet'): ").strip() or "None yet"
    cost = input("Cost (e.g., TBD, $10.50) [TBD]: ").strip() or "TBD"
    
    actual_owner = owner_input or "Unknown"

    print("\nContributors (enter one per line, blank line to finish):")
    contributors_list = []
    while True:
        contributor = input("  Contributor name (or blank to finish): ").strip()
        if not contributor:
            break
        contributors_list.append(contributor)
    
    if not contributors_list:
        if owner_input: # If user provided an owner name (not blank)
            contributors_list = [owner_input]
        # If owner_input was blank, and no contributors, list remains empty.

    return {
        'part_number': part_number_str,
        'owner': actual_owner,
        'name': name or "Unnamed Part",
        'description': description or "No description provided.",
        'parent_assembly': parent_assembly,
        'status': status,
        'part_type': part_type,
        'alternatives': alternatives_list, # Will be [] if none added
        'primary_source': primary_source or "Unknown",
        'secondary_source': secondary_source,
        'cost': cost,
        'contributors': contributors_list, 
        # 'date_created': datetime.date.today().isoformat() # Removed date_created
    }

def main():
    print("Hardware Part Creator Utility")
    print("-----------------------------")
    print("This script will help you create a new part directory and metadata.yaml file.")
    # PyYAML import check is at the top of the file

    project_root = get_project_root()
    print(f"Project root identified as: {project_root}")

    existing_parts = get_existing_part_numbers(project_root)
    print(f"Found existing part numbers: {sorted(list(existing_parts)) if existing_parts else 'None'}")

    new_part_number = generate_unique_part_number(existing_parts)
    part_number_str = str(new_part_number)
    print(f"\nGenerated new part number: {part_number_str}")

    part_dir_path = os.path.join(project_root, part_number_str)

    if os.path.exists(part_dir_path):
        print(f"Error: Directory {part_dir_path} already exists. This should not happen if generation logic is correct.")
        sys.exit(1)

    metadata = prompt_for_metadata(part_number_str)

    try:
        os.makedirs(part_dir_path)
        print(f"\nSuccessfully created directory: {part_dir_path}")
    except OSError as e:
        print(f"Error creating directory {part_dir_path}: {e}")
        sys.exit(1)

    metadata_file_path = os.path.join(part_dir_path, 'metadata.yaml')
    try:
        with open(metadata_file_path, 'w', encoding='utf-8') as f:
            yaml.dump(metadata, f, sort_keys=False, indent=2, default_flow_style=False, allow_unicode=True)
        print(f"Successfully created metadata file: {metadata_file_path}")
    except Exception as e:
        print(f"Error writing metadata file {metadata_file_path}: {e}")
        sys.exit(1)
        
    print("\nPart creation process complete!")
    print(f"A new directory '{part_number_str}' with 'metadata.yaml' has been created in '{project_root}'.")
    print("You can now add your CAD files (e.g., .step, .stl) to this directory.")

if __name__ == "__main__":
    main()
