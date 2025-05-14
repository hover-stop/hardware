import os
import sys
import datetime

try:
    import yaml
except ImportError:
    print("Error: PyYAML library not found. Please install it by running: pip install PyYAML")
    sys.exit(1)

def get_project_root():
    """Determines the project root directory (assumed to be parent of 'utils')."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(script_dir)

def find_metadata_files(project_root):
    """Finds all metadata.yaml files in part directories."""
    metadata_files = []
    for item in os.listdir(project_root):
        item_path = os.path.join(project_root, item)
        # Check if item is a directory, is a 5-digit number (part number)
        if os.path.isdir(item_path) and item.isdigit() and len(item) == 5:
            metadata_path = os.path.join(item_path, 'metadata.yaml')
            if os.path.isfile(metadata_path):
                metadata_files.append(metadata_path)
    return metadata_files

def generate_bom_markdown(metadata_files):
    """Generates a Markdown BOM from a list of metadata files."""
    bom_items = []
    for mf_path in metadata_files:
        try:
            with open(mf_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                if data:
                    bom_items.append({
                        'part_number': str(data.get('part_number', 'N/A')),
                        'name': data.get('name', 'N/A'),
                        'description': data.get('description', 'N/A'),
                        'quantity': data.get('quantity', 1), # Default to 1 if not specified
                        'part_type': data.get('part_type', 'N/A'),
                        'primary_source': data.get('primary_source', 'N/A'),
                        'cost': data.get('cost', 'N/A'),
                        'owner': data.get('owner', 'N/A'),
                        'status': data.get('status', 'N/A')
                    })
        except Exception as e:
            print(f"Warning: Could not process file {mf_path}: {e}")

    if not bom_items:
        return "# Bill of Materials\n\nNo parts found or metadata files are empty/corrupted.\n"

    # Sort by part number
    bom_items.sort(key=lambda x: x['part_number'])

    # Create Markdown table
    headers = ["Part Number", "Name", "Description", "Qty", "Part Type", "Primary Source", "Cost", "Owner", "Status"]
    md_table = f"# Bill of Materials\n\nGenerated on: {datetime.date.today().isoformat()}\n\n"
    md_table += "| " + " | ".join(headers) + " |\n"
    md_table += "| " + " | ".join(["---"] * len(headers)) + " |\n"

    for item in bom_items:
        row = [
            item['part_number'],
            item['name'],
            item['description'],
            str(item['quantity']),
            item['part_type'],
            item['primary_source'],
            str(item['cost']),
            item['owner'],
            item['status']
        ]
        md_table += "| " + " | ".join(row) + " |\n"
    
    return md_table

def main():
    print("Bill of Materials Generator")
    print("---------------------------")

    project_root = get_project_root()
    print(f"Project root identified as: {project_root}")

    metadata_files = find_metadata_files(project_root)
    if not metadata_files:
        print("No metadata.yaml files found in part directories.")
        # Create an empty BOM.md or one with a message
        bom_content = "# Bill of Materials\n\nNo part metadata files found.\n"
    else:
        print(f"Found {len(metadata_files)} metadata files. Processing...")
        bom_content = generate_bom_markdown(metadata_files)

    bom_file_path = os.path.join(project_root, 'BOM.md')
    try:
        with open(bom_file_path, 'w', encoding='utf-8') as f:
            f.write(bom_content)
        print(f"Successfully generated BOM: {bom_file_path}")
    except Exception as e:
        print(f"Error writing BOM file {bom_file_path}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
