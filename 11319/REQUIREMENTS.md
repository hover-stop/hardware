# Requirements for 11319 - Throttle Body Bottom Plate

This document outlines the key design and functional requirements for the Throttle Body Bottom Plate (Part Number 11319).

## Functional Requirements

1.  **Structural Base:** Shall serve as the primary structural base for the `96784 - HSI Mk.1 Body Assembly`.
2.  **Component Mounting:** Must provide robust and accurate mounting points for:
    *   Top facia panels.
    *   Internal throttle mechanisms (e.g., lever assemblies, sensors, friction systems).
    *   Any other components directly part of the core throttle body.
3.  **Load Bearing:** Must be capable of supporting the loads exerted by user operation of the throttle controls and the weight of attached components.
4.  **Serviceability:** Design should allow for access to and servicing of internal components attached to this plate.

## Physical & Manufacturing Requirements

1.  **Primary Manufacturing Process:** Intended to be `3D Printed` (as per metadata). Alternative manufacturing considerations can be noted if applicable.
2.  **Material:** To be specified (e.g., PETG, ABS, PLA+ with sufficient strength and rigidity).
3.  **Dimensional Stability:** Must maintain dimensional accuracy to ensure proper fit and alignment of all attached parts and external mounting interfaces.
4.  **Heat Resistance:** If in proximity to electronics or other heat sources, material selection should consider heat resistance.

## Interfacing & Mounting Requirements

This plate is designed for versatile mounting and must provide features to interface with the following (mutually exclusive mounting methods):

1.  **Enclosure Mounting (via `42807 - Mounting Tray`):**
    *   Shall provide defined mounting points (e.g., holes, bosses) to securely attach to the `42807 - Mounting Tray` (the "purple brace").
    *   These mounting points must align with the corresponding features on the `42807 - Mounting Tray`.
2.  **DZUS Rail Mounting:**
    *   Shall incorporate features compatible with standard DZUS rails for direct mounting (if this option is chosen).
    *   This may include specific hole patterns, thicknesses, or edge features.
3.  **Custom Flat Panel Mounting:**
    *   Shall provide a pattern of mounting holes (e.g., 6 or more, as per Xpendable's notes) allowing it to be screwed down onto a custom flat surface (e.g., wood, MDF, metal plate).
    *   These holes should be accessible from the top (through the facia or before facia installation).
    *   The design should consider necessary cutouts in the custom panel for throttle mechanism clearance, mimicking openings in the `42807 - Mounting Tray`.

## Assembly & Hierarchy

1.  **Parent Assembly:** This part is a critical component of `96784 - Body Assembly`.
2.  **Fastening Methods:** Should utilize appropriate fastening methods for all attached components (e.g., heat-set inserts for machine screws, self-tapping screws for plastic if suitable, through-holes for bolts).

## Design Considerations

*   Minimize weight while maintaining structural integrity.
*   Ensure clearance for all moving parts of the throttle mechanisms.
*   Consider wire routing and management if electronics are mounted directly or pass through.
