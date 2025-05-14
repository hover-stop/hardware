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

# Updated helper function to recursively build the tree string
def _build_tree_recursive_str(part_number, parts_data, indent_prefix, is_last_sibling, visited_for_path):
    part_info = parts_data.get(part_number)
    line_connector = "└── " if is_last_sibling else "├── "

    if not part_info:
        return indent_prefix + line_connector + f"{part_number} - [Data Missing for this Part]\n"

    if part_number in visited_for_path:
        display_name_cycle = part_info.get('name', '[Name Missing]')
        return indent_prefix + line_connector + f"{part_number} - {display_name_cycle} ... [Circular reference detected]\n"
    
    visited_for_path.add(part_number)
    
    display_name = part_info.get('name', '[Name Missing]')
    tree_str = indent_prefix + line_connector + f"{part_number} - {display_name}\n"
    
    children = sorted(part_info.get('children', []))
    num_children = len(children)

    # Determine the prefix for the children's lines
    new_indent_for_children = indent_prefix + ("    " if is_last_sibling else "│   ")

    for i, child_pn in enumerate(children):
        is_child_last_sibling = (i == num_children - 1)
        tree_str += _build_tree_recursive_str(child_pn, parts_data, new_indent_for_children, is_child_last_sibling, visited_for_path.copy())
            
    return tree_str

# Updated function to generate the Markdown section for the part assembly tree
def generate_part_tree_markdown_section(bom_items_list):
    part_tree_md = "\n## Part Assembly Tree\n\n```\n" # Start Markdown code block
    
    if not bom_items_list:
        part_tree_md += "No parts data available to build a tree.\n"
        part_tree_md += "```\n" # End code block
        return part_tree_md

    parts_data = {}
    # Initial population of parts_data from actual metadata
    for item in bom_items_list:
        pn = str(item.get('part_number', 'N/A'))
        if pn == 'N/A': continue
        parts_data[pn] = {
            'name': item.get('name', '[No Name]'),
            'parent_assembly': str(item.get('parent_assembly')) if item.get('parent_assembly') is not None and str(item.get('parent_assembly')).strip() != "" else 'None',
            'children': [],
            'is_placeholder': False 
        }

    # Second pass to build hierarchy and create placeholders for missing parents
    all_part_numbers_from_metadata = set(parts_data.keys())
    
    for pn_from_meta in list(all_part_numbers_from_metadata): 
        if pn_from_meta not in parts_data or parts_data[pn_from_meta].get('is_placeholder', True):
            continue

        data = parts_data[pn_from_meta]
        parent_pn_str = data['parent_assembly']

        if parent_pn_str != 'None':
            if parent_pn_str not in parts_data: 
                parts_data[parent_pn_str] = {
                    'name': '[External/Missing Parent]',
                    'parent_assembly': 'None', 
                    'children': [pn_from_meta],
                    'is_placeholder': True
                }
            else: 
                if pn_from_meta not in parts_data[parent_pn_str]['children']:
                     parts_data[parent_pn_str]['children'].append(pn_from_meta)
    
    all_child_pns = set()
    for pn_key in parts_data:
        for child_pn in parts_data[pn_key].get('children', []):
            all_child_pns.add(child_pn)
            
    root_pns = []
    for pn_key in parts_data:
        if pn_key not in all_child_pns:
            root_pns.append(pn_key)
    
    sorted_root_pns = sorted(list(set(root_pns)))

    if not sorted_root_pns:
        if parts_data: 
            part_tree_md += "No top-level assemblies identified. All parts may be interconnected or form cycles.\n"
        else:
             part_tree_md += "No parts data to build tree from.\n"
    else:
        num_roots = len(sorted_root_pns)
        for i, root_pn in enumerate(sorted_root_pns):
            root_info = parts_data.get(root_pn)
            if not root_info: continue
            
            # Print the root item name
            part_tree_md += f"{root_pn} - {root_info.get('name', '[Name Missing]')}\n"
            
            children_of_root = sorted(root_info.get('children', []))
            num_children_of_root = len(children_of_root)

            for j, child_pn in enumerate(children_of_root):
                is_child_last_sibling = (j == num_children_of_root - 1)
                # Children of the root start with an empty initial indent_prefix from this level;
                # _build_tree_recursive_str will add the appropriate connector.
                part_tree_md += _build_tree_recursive_str(child_pn, parts_data, "", is_child_last_sibling, set()) 
            
            # Add a blank line between trees if there are multiple root assemblies and this isn't the last one
            if num_roots > 1 and i < num_roots - 1:
                part_tree_md += "\n"
            
    part_tree_md += "```\n" # End Markdown code block
    return part_tree_md

def generate_bom_markdown(metadata_files):
    """Generates a Markdown BOM and Part Tree from a list of metadata files."""
    bom_items_list = []
    for mf_path in metadata_files:
        try:
            with open(mf_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                if data:
                    # Ensure parent_assembly is read as a string, handle None or empty
                    parent_assembly_raw = data.get('parent_assembly')
                    parent_assembly_str = str(parent_assembly_raw) if parent_assembly_raw is not None and str(parent_assembly_raw).strip() != "" else 'None'

                    bom_items_list.append({
                        'part_number': str(data.get('part_number', 'N/A')),
                        'name': data.get('name', 'N/A'),
                        'description': data.get('description', 'N/A'),
                        'quantity': data.get('quantity', 1), 
                        'part_type': data.get('part_type', 'N/A'),
                        'primary_source': data.get('primary_source', 'N/A'),
                        'cost': data.get('cost', 'N/A'),
                        'owner': data.get('owner', 'N/A'),
                        'status': data.get('status', 'N/A'),
                        'parent_assembly': parent_assembly_str
                    })
        except Exception as e:
            print(f"Warning: Could not process file {mf_path}: {e}")

    if not bom_items_list:
        return """<!-- 
THIS FILE IS AUTO-GENERATED BY THE cli_make_bom.py SCRIPT.
DO NOT EDIT THIS FILE MANUALLY. YOUR CHANGES WILL BE OVERWRITTEN.
-->

# Bill of Materials

Generated on: {datetime.date.today().isoformat()}

No parts found or metadata files are empty/corrupted.
"""

    # Sort BOM items by part number for the table
    bom_items_list.sort(key=lambda x: x['part_number'])

    # Create Markdown table for BOM
    headers = ["Part Number", "Name", "Description", "Qty", "Part Type", "Primary Source", "Cost", "Owner", "Status"]
    md_output = f"""<!-- 
THIS FILE IS AUTO-GENERATED BY THE cli_make_bom.py SCRIPT.
DO NOT EDIT THIS FILE MANUALLY. YOUR CHANGES WILL BE OVERWRITTEN.
-->

# Bill of Materials

Generated on: {datetime.date.today().isoformat()}

"""
    md_output += "| " + " | ".join(headers) + " |\n"
    md_output += "| " + " | ".join(["---"] * len(headers)) + " |\n"

    for item in bom_items_list:
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
        md_output += "| " + " | ".join(row) + " |\n"
    
    # Generate and append Part Tree section
    # The bom_items_list already contains all necessary info including parent_assembly
    part_tree_section_md = generate_part_tree_markdown_section(bom_items_list)
    md_output += part_tree_section_md

    return md_output

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
