# Requirements for 42807 - Mounting Tray (Purple Brace)

This document outlines the key design and functional requirements for the Mounting Tray (Part Number 42807), also referred to as the "purple brace". This tray is specifically used when mounting the HSI Mk.1 throttle assembly within a custom enclosure.

## Functional Requirements

1.  **Enclosure Mounting Interface:** Shall serve as the structural interface between the HSI Mk.1 `96784 - Body Assembly` (specifically, its bottom plate) and a custom enclosure.
2.  **Replaces Rails for Enclosure Use:** When this tray is used, DZUS rails are not needed for mounting the throttle body. This tray provides the necessary support and attachment points within the enclosure.
3.  **Serviceability:** Must allow for the HSI Mk.1 Body Assembly to be installed and removed from the enclosure without damaging the tray or the enclosure.
4.  **Rigidity:** Must provide a rigid and stable platform for the HSI Mk.1 Body Assembly when installed in an enclosure.
5.  **Clearance for Components:** Must provide adequate openings and clearances for any cables or components protruding from the bottom of the HSI Mk.1 Body Assembly.

## Physical & Manufacturing Requirements

1.  **3D Printability:** Must be manufacturable as a single piece via 3D printing on a print bed with dimensions of at least 256x256mm (if applicable, or specify other manufacturing process).
2.  **Material:** To be specified (e.g., PETG, ABS, PLA+).
3.  **Dimensional Constraints:** Overall dimensions must be compatible with the intended enclosure design and the `77875 - Ghost Volume, Throttle Body` if it represents the enclosure's internal space.

## Assembly & Hierarchy

1.  **Parent Assembly:** This part is a component of `62988 - HSI Mk.1 Mounting Kit`.
2.  **Mounting Method:** Attaches to the custom enclosure structure (method to be defined) and provides mounting points for the HSI Mk.1 `96784 - Body Assembly` (via its bottom plate).

## Exclusions

*   This part is **not** used if the HSI Mk.1 throttle is mounted using DZUS rails.
*   This part is **not** used if the HSI Mk.1 throttle is mounted directly to a custom panel (e.g., a sheet of wood/MDF) without an enclosure.
