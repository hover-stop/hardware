# HSI Mk1 Hardware Repository

This repository contains the hardware design files for the HoverStop project. It includes part files, metadata, and utility scripts to manage and validate the hardware components.

---

## Documentation

For detailed design guidelines, part requirements, and contribution processes, please visit our [documentation site](https://hover-stop.github.io/docs/).

---

## Repository Structure

Each part is stored in its own folder named with a 5-digit part number. The folder contains:

- Design files (e.g., `.step`, `.3mf`)
- `metadata.yaml` file with part details
- Optional `REQUIREMENTS.md` file for part-specific requirements

---

## Utility Scripts

The `utils/` directory contains scripts to automate common tasks:

- **`cli_new_part.py`**: Automates the creation of new part directories with unique part numbers.
- **`cli_make_bom.py`**: Generates a Bill of Materials (`BOM.md`) from all `metadata.yaml` files.
- **`cli_validate_metadata.py`**: Validates `metadata.yaml` files against a defined schema.

Refer to the `utils/README.md` file for setup and usage instructions.

---

## Contribution Workflow

1. Create a new branch for your changes.
2. Use `cli_new_part.py` to add new parts.
3. Validate your changes with `cli_validate_metadata.py`.
4. Generate the BOM using `cli_make_bom.py`.
5. Submit a pull request for review.

---

## Communication

All major updates and discussions are coordinated via Discord. For questions or support, please reach out to the team.
