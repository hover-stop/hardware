# HSI Mk1 Hardware Design Guide

This guide defines how we design, document, and manage the hardware for the HoverStop project. It ensures consistency, version control, and collaboration across contributors.

---

## Units

- All measurements and dimensions must be in **millimeters (mm)**.

---

## Repository Structure

- All parts and assemblies are stored in the GitHub hardware repository.
- Git is the **single source of truth** for design files and history.

---

## File Structure

Each part will live in its own folder named with a 5-digit part number:

Example folder structure:

```
/12345/
  ├── 12345 - Mounting Bracket.step
  ├── 12345 - Mounting Bracket.3mf
  ├── metadata.yaml
  └── 12345 - Mounting Bracket.pdf (drawing)
```

**metadata.yaml** will contain:

```
part_number: 12345
owner: Engines
description: Steel bracket that supports the nozzle stop block
parent_assembly: 12000
status: Release
primary_source: https://mcmaster.com/1234
secondary_source: https://digikey.com/xyz
cost: 4.25
contributors:
  - Engines
  - Carpet3
```

---

## Drawing Requirements

- Every **part** must have a detailed drawing specifying:
  - Dimensions
  - Tolerances
  - Critical features

- Every **assembly** must also include:
  - A complete exploded or assembled view drawing
  - Fastener and hardware BOM (bill of materials)

- Drawings will be published to Discord for reference

---

## Part Numbering

- Every new part is assigned a **unique random 5-digit number**
- The number is the primary ID and **must appear in the file names and metadata**
- No version letters or suffixes should be used (e.g., “rev A”)

---

## Revision Control

- No manual revision numbers
- All versioning is handled through **Git**
- Commit history and branches reflect all changes and approvals

---

## Status Tags

Parts must have one of the following statuses in `metadata.yaml`:

- `Draft` – initial concept or WIP
- `Review` – under review by others
- `Release` – approved and finalized for build or print

---

## Release Criteria

A part can be considered “released” when:

- A `.step` file is present and accurate
- A `.3mf` (or equivalent 3D printing format) is provided
- A detailed part drawing is completed and reviewed
- A drawing of the full assembly (if applicable) is provided
- A `metadata.yaml` is fully filled in
- If applicable, a tested `.gcode` file is also included

---

## General Design Guidance

- Avoid reinventing the wheel — use existing parts or designs where possible
- Standardize common parts and **include sources** in metadata
- Prefer off-the-shelf components and consumables when it simplifies builds
- Each project will have a **ghost assembly**, aka a “Bitkit,” which represents a reusable collection of fasteners or consumables

---

## Contribution & Versioning

- All changes must go through **Git** (e.g., via PRs or commits to main)
- Contributors should be listed in the part’s `metadata.yaml`
- To contribute:
  - Create a working branch
  - Commit changes
  - Create a PR to `main`
  - Once reviewed, changes are merged into `main`

---

## Release Branch Process

We maintain a clean separation of work and released output.

```
main → reviewed and tested parts
release → officially published, tagged versions
working branches → individual development (e.g. `feature/nozzle-block`)
```

When a part is finalized:

1. Reviewed and merged to `main`
2. Included in a release commit to `release`
3. Tagged in Git with a version tag (e.g. `v1.0.3`)
4. Posted in Discord with release notes

---

## Communication & Coordination

- All major updates are posted to Discord
- Release announcements are published to the community
- Questions, suggestions, and discussions occur in relevant Discord threads
