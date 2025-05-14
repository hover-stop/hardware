import os
import sys
import datetime
import random # Added import for random number generation
import argparse # Added for command-line argument parsing
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

def load_metadata(file_path):
    """Loads metadata from a YAML file."""
    if not os.path.exists(file_path):
        print(f"Error: Metadata file not found at {file_path}")
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML from {file_path}: {e}")
        return None
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def prompt_for_metadata(part_number_str, cloned_metadata=None):
    """Prompts the user for part metadata, using cloned_metadata for defaults if provided."""
    print("\nPlease enter the following metadata for the new part:")

    def get_default(key, default_value=""):
        if cloned_metadata and key in cloned_metadata:
            return cloned_metadata[key]
        return default_value

    owner_input = input(f"Owner (e.g., Kurisu) [{get_default('owner')}]: ").strip() or get_default('owner')
    name = input(f"Part Name (e.g., Main Body - do not include part number '{part_number_str}') [{get_default('name')}]: ").strip() or get_default('name')
    description = input(f"Description [{get_default('description')}]: ").strip() or get_default('description')
    parent_assembly_default = get_default('parent_assembly', "None")
    parent_assembly = input(f"Parent Assembly (e.g., 31000, or 'None') [{parent_assembly_default}]: ").strip() or parent_assembly_default
    
    status_default = get_default('status', "Draft")
    status = input(f"Status (e.g., Draft, Review, Release, Prototype, Obsolete, In Development) [{status_default}]: ").strip() or status_default
    
    part_type_default = get_default('part_type', "3D Printed")
    part_type = input(f"Part Type (e.g., 3D Printed, Machined, Off The Shelf) [{part_type_default}]: ").strip() or part_type_default

    print("\nAlternatives (enter one per line, blank line to finish):")
    alternatives_list = []
    cloned_alternatives = get_default('alternatives', [])
    if cloned_alternatives:
        print(f"  Cloned alternatives: {cloned_alternatives} (Press Enter to keep, type new to override)")
        # Simple override: if user types anything, they start fresh for alternatives.
        # More sophisticated merging could be added if needed.
        user_input_for_alt = input("  Press Enter to keep cloned alternatives, or type 'new' to define new ones: ").strip()
        if not user_input_for_alt:
            alternatives_list = cloned_alternatives
        else: # User wants to define new ones
            cloned_alternatives = [] # Clear cloned so the loop below runs for new input
    
    if not alternatives_list and not cloned_alternatives: # Only prompt if not kept from clone or clone had none
        while True:
            alt_desc = input("  Alternative Description (or blank to finish): ").strip()
            if not alt_desc:
                break
            alt_source_default = "To be determined"
            # Check if this specific alternative existed in clone to suggest its source (more complex logic)
            # For simplicity, we're not pre-filling individual alternative sources from clone here if user re-enters
            alt_source = input(f"  Source for '{alt_desc}' [{alt_source_default}]: ").strip() or alt_source_default
            alternatives_list.append({'description': alt_desc, 'source': alt_source})
        
    primary_source_default = get_default('primary_source', "Unknown")
    primary_source = input(f"Primary Source (e.g., In-house prototype, Vendor XYZ) [{primary_source_default}]: ").strip() or primary_source_default
    
    secondary_source_default = get_default('secondary_source', "None yet")
    secondary_source = input(f"Secondary Source (or 'None yet') [{secondary_source_default}]: ").strip() or secondary_source_default
    
    cost_default = get_default('cost', "TBD")
    cost_input = input(f"Cost (e.g., TBD, 10.50) [{cost_default}]: ").strip() or str(cost_default) # Ensure it's a string for TBD
    
    quantity_default = get_default('quantity', 1)
    while True:
        try:
            quantity_input = input(f"Quantity (integer, minimum 1) [{quantity_default}]: ").strip()
            quantity = int(quantity_input or quantity_default)
            if quantity < 1:
                print("  Quantity must be 1 or greater.")
            else:
                break
        except ValueError:
            print("  Invalid input. Please enter an integer for quantity.")

    actual_owner = owner_input or "Unknown"

    print("\nContributors (enter one per line, blank line to finish):")
    contributors_list = []
    cloned_contributors = get_default('contributors', [])
    if cloned_contributors:
        print(f"  Cloned contributors: {', '.join(cloned_contributors)}. (Press Enter to keep, type new to override)")
        user_input_for_contrib = input("  Press Enter to keep cloned contributors, or type 'new' to define new ones: ").strip()
        if not user_input_for_contrib:
            contributors_list = cloned_contributors
        else: # User wants to define new ones
            cloned_contributors = [] # Clear for new input loop

    if not contributors_list and not cloned_contributors: # Only prompt if not kept from clone or clone had none
        while True:
            contributor = input("  Contributor name (or blank to finish): ").strip()
            if not contributor:
                break
            contributors_list.append(contributor)
    
    if not contributors_list and not cloned_contributors: # If still empty after prompts
        if actual_owner and actual_owner != "Unknown":
            contributors_list = [actual_owner]
        # If owner_input was blank, and no contributors, list remains empty.

    return {
        'part_number': part_number_str,
        'owner': actual_owner,
        'name': name or "Unnamed Part",
        'description': description or "No description provided.",
        'parent_assembly': parent_assembly,
        'status': status,
        'part_type': part_type,
        'alternatives': alternatives_list,
        'primary_source': primary_source,
        'secondary_source': secondary_source,
        'cost': cost_input, # Use the input which could be "TBD" or a number as string
        'quantity': quantity,
        'contributors': contributors_list or ([actual_owner] if actual_owner and actual_owner != "Unknown" else [])
    }

def main():
    parser = argparse.ArgumentParser(description="Hardware Part Creator Utility")
    parser.add_argument("--clone", type=str, help="Part number to clone metadata from (e.g., 12345)")
    args = parser.parse_args()

    print("Hardware Part Creator Utility")
    print("-----------------------------")
    print("This script will help you create a new part directory and metadata.yaml file.")
    # PyYAML import check is at the top of the file

    project_root = get_project_root()
    print(f"Project root identified as: {project_root}")

    cloned_data = None
    if args.clone:
        print(f"\nAttempting to clone metadata from part number: {args.clone}")
        if not (args.clone.isdigit() and len(args.clone) == 5):
            print(f"Error: Cloned part number '{args.clone}' must be a 5-digit number.")
            sys.exit(1)
        
        clone_metadata_path = os.path.join(project_root, args.clone, 'metadata.yaml')
        cloned_data = load_metadata(clone_metadata_path)
        if cloned_data:
            print(f"Successfully loaded metadata from {args.clone}.")
            # Remove part_number from cloned data so it doesn't overwrite the new one by mistake
            if 'part_number' in cloned_data:
                del cloned_data['part_number'] 
        else:
            print(f"Warning: Could not load metadata from part {args.clone}. Proceeding without defaults.")

    existing_parts = get_existing_part_numbers(project_root)
    print(f"Found existing part numbers: {sorted(list(existing_parts)) if existing_parts else 'None'}")

    new_part_number = generate_unique_part_number(existing_parts)
    part_number_str = str(new_part_number)
    print(f"\nGenerated new part number: {part_number_str}")

    part_dir_path = os.path.join(project_root, part_number_str)

    if os.path.exists(part_dir_path):
        print(f"Error: Directory {part_dir_path} already exists. This should not happen if generation logic is correct.")
        sys.exit(1)

    metadata = prompt_for_metadata(part_number_str, cloned_data)

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
