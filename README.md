# HSI Mk1 Hardware Design Guide

This guide defines how we design, document, and manage the hardware for the HoverStop project. It ensures consistency, version control, and collaboration across contributors.

---

## Units

* All measurements and dimensions must be in **millimeters (mm)**.

---

## Repository Structure

* All parts and assemblies are stored in the GitHub hardware repository.
* Git is the **single source of truth** for design files and history.

---

## File Structure

Each part will live in its own folder named with a 5-digit part number:

Example folder structure:

```
/12345/
  ├── 12345-Mounting Bracket.step
  ├── 12345-Mounting Bracket.3mf
  ├── metadata.yaml
  ├── REQUIREMENTS.md  # Recommended: Part-specific requirements
  └── 12345-Mounting Bracket.pdf (drawing)
```

**metadata.yaml** will contain:

The structure of this file is enforced by the `utils/cli_validate_metadata.py` script.

```yaml
part_number: "12345" # Must be a 5-digit string matching the folder name
owner: "Engines"
name: "Mounting Bracket Example"
description: "Steel bracket that supports the nozzle stop block"
parent_assembly: "12000" # 5-digit part number of parent or "None"
status: "Release" # See "Status Tags" section for allowed values
part_type: "Machined" # See "Part Types" section for allowed values
primary_source: "https://mcmaster.com/1234"
secondary_source: "https://digikey.com/xyz" # Can be "None yet" or similar if not applicable
cost: "4.25" # Can be a number or string like "TBD"
quantity: 1 # Integer, minimum 1
alternatives:
  - description: "Equivalent part from local supplier"
    source: "https://localvendor.com/part"
  # - description: "Another alternative"
  #   source: "Link or description"
contributors:
  - "Engines"
  - "Carpet3"
```

---

## Part Requirements Documentation (Recommended)

It is highly recommended to include a `REQUIREMENTS.md` file within each part's directory. This file should summarize the key design, functional, physical, and manufacturing requirements for that specific part. 

This practice helps ensure clarity on the part's purpose and constraints, aiding in design, review, and future modifications.

An example structure for `REQUIREMENTS.md` could be:

```markdown
# Requirements for [Part Number] - [Part Name]

This document outlines the key design and functional requirements for the [Part Name] (Part Number [Part Number]).

## Functional Requirements

1.  **Primary Function:** [Description]
2.  **Interaction with Other Parts:** [Details]
3.  **Performance Metric 1:** [Target]

## Physical & Manufacturing Requirements

1.  **Material:** [Specified material]
2.  **Manufacturing Process:** [e.g., 3D Printed, Machined]
3.  **Key Dimensions/Tolerances:** [Details]
4.  **Constraint 1:** [e.g., Max weight, size envelope]

## Assembly & Hierarchy

1.  **Parent Assembly:** [Part Number of parent assembly]
2.  **Mounting Method:** [How it attaches]

## Serviceability & Durability

1.  **Expected Lifespan:** [Time/cycles]
2.  **Maintenance Needs:** [Details]
```

This template can be adapted as needed for the specific part.

---

## Utility Scripts

The `utils/` directory in this repository contains helpful command-line scripts to automate common tasks:

*   **`cli_new_part.py`**: This script automates the creation of new part directories. It generates a unique random 5-digit part number, creates the correspondingly named folder, and populates it with a basic `metadata.yaml` file after prompting the user for necessary information.
*   **`cli_make_bom.py`**: This script scans all part `metadata.yaml` files to generate a comprehensive Bill of Materials (`BOM.md`) in the project root. The `BOM.md` includes a table of all parts and a hierarchical Part Assembly Tree.
*   **`cli_validate_metadata.py`**: This script validates all `metadata.yaml` files against a defined schema to ensure consistency and correctness. It checks for required fields, data types, and specific allowed values.

For detailed instructions on setting up the Python environment for these scripts and their usage, please refer to the `utils/README.md` file.

---

## Drawing Requirements

* Every **part** must have a detailed drawing specifying:

  * Dimensions
  * Tolerances (especially on mating surfaces, press fits, and interfaces)
  * Critical features (holes, mounting surfaces, alignment interfaces)

* Every **assembly** must also include:

  * A complete exploded or assembled view drawing
  * Fastener and hardware BOM (bill of materials)

* Drawings will be published to Discord for reference

Default tolerance: **±0.2mm** unless otherwise specified.

---

## Part Numbering

* Every new part is assigned a **unique random 5-digit number** using the `utils/cli_new_part.py` script.
* This tool helps prevent part number collisions.
* Contributors should use this script to ensure consistency when creating new parts.

---

## Revision Control

* No manual revision letters or numbers
* All versioning is handled through **Git commit history**
* Contributions are tracked by name in `metadata.yaml`

---

## Status Tags

Parts must have one of the following statuses in their `metadata.yaml` file. This is enforced by the `utils/cli_validate_metadata.py` script.

* `Draft`
* `Review`
* `Release`
* `Prototype`
* `Obsolete`
* `In Development`

---

## Release Criteria

A part can be considered "released" when:

* A valid `.step` file exists
* A `.3mf` or `.stl` file is provided (if 3D printed)
* A detailed part drawing is complete and reviewed
* A drawing of the full assembly is provided (if applicable)
* The `metadata.yaml` is complete and includes:

  * Material and process type (e.g., Machined, 3D Printed)
  * Primary/secondary sources
  * Cost info
  * Alternative sourcing

Note: **G-code is not required**, as it varies too much between printers.

---

## General Design Guidance

* Avoid reinventing the wheel — reuse existing parts when practical
* Use standard hardware from the shared Bitkit whenever possible
* Off-the-shelf parts must include supplier info in metadata
* Contributors are encouraged to propose new Bitkit parts via PRs

### Part Types (for `part_type` in metadata.yaml):

The following are the allowed values for the `part_type` field. This is enforced by the `utils/cli_validate_metadata.py` script.

* `3D Printed`
* `Machined`
* `Off The Shelf`
* `Sheet Metal`
* `Electronics`
* `Cable or Wire`
* `Assembly`
* `Ghost`
* `None`
* `Other`

---

## Contribution & Versioning

* All design updates must go through **Git**
* Contributors are listed in each part's `metadata.yaml`
* Use branches to manage changes:

```
main → reviewed and validated parts
dev branches → in-progress edits or features
release → clean, tagged snapshots of released components
```

---

## Release Process

1. Contributor makes change in feature branch
2. Pull request opens to `main`, reviewed by peers
3. Once approved, merged into `main`
4. At regular intervals, parts are merged into `release` and tagged (e.g., `v1.0.2`)
5. Release notes posted to Discord with list of updated parts

---

## Communication

* All major changes, releases, and decisions are posted in Discord
* Thread-based discussions encouraged per part or topic
* New part numbers and assignments are coordinated via GitHub or Discord
