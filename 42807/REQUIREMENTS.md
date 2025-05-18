# Requirements for 42807 - Case Adapter (formerly "Mounting Tray" / "Purple Brace")

This document outlines the key design and functional requirements for the **Case Adapter** (Part Number 42807), which is used when mounting the HSI Mk.1 throttle assembly inside a custom enclosure. This adapter interfaces between the enclosure and the base plate but **does not support** the throttle body directly.

## Functional Requirements

1. **Enclosure Mounting Interface:** Shall provide a rigid mounting surface for custom enclosure side panels to attach to, enabling enclosed use of the HSI Mk.1 throttle system.
2. **Supports Base Plate, Not Throttle:** Does **not** directly support the `96784 - Body Assembly` (i.e., the throttle mechanism). Instead, the base plate rests on top of this adapter.
3. **Replaces DZUS Rails in Case Use:** When this adapter is used, DZUS rails are not required. It fulfills the structural interface role within enclosed applications.
4. **Serviceability:** Must allow the HSI Mk.1 base plate (with attached throttle components) to be installed or removed without damage to the case or adapter.
5. **Clearance:** Must not interfere with components protruding below the base plate (e.g., wiring, connectors).

## Physical & Manufacturing Requirements

1. **3D Printability:** Must be manufacturable as a single piece via 3D printing on beds with dimensions ≥256x256mm.
2. **Material:** To be determined (recommended: PETG or ABS for structural integrity).
3. **Dimensional Fit:** Overall dimensions must align with the internal volume defined by `77875 - Ghost Volume, Throttle Body`, and allow the base plate to sit flush above it.

## Assembly & Hierarchy

1. **Parent Assembly:** Component of `62988 - HSI Mk.1 Mounting Kit`.
2. **Mounting Method:** Attaches to the enclosure structure. Provides a support interface for the `Base Plate` (separately defined), not for the `96784 - Body Assembly` directly.

## Naming and Clarification

* This part shall be referred to as the **Case Adapter**.
* It is **not** to be confused with the **Base Plate** (which the throttle assembly bolts to).
* The **Base Plate** is a separate part that sits on top of this adapter inside the enclosure.

## Exclusions

* Not used if throttle is mounted using DZUS rails or custom mounting rails.
* Not used if the throttle is panel-mounted directly to a desk, MDF, or cockpit structure.
