# Requirements for 42807 - Case Adapter (formerly "Mounting Tray" / "Purple Brace")

This document outlines the key design and functional requirements for the **Case Adapter** (Part Number 42807), previously referred to as the "mounting tray" or "purple brace". This adapter is used only when the HSI Mk.1 throttle is enclosed within the HSI case, and serves as the interface between the throttle base plate and the case walls.

## Functional Requirements

1. **Case-to-Throttle Interface:** Shall provide a structural interface between the HSI Mk.1 **Base Plate** (to which all throttle components are mounted) and the **case walls**, enabling the throttle to be enclosed.
2. **Used Only with Case:** This adapter is only used when the throttle is mounted **within the HSI case**. It is not compatible with DZUS rail mounting or standalone tray installations.
3. **Supports Base Plate:** Provides support under the **Base Plate**, but does not directly attach to the throttle internals (`96784 - Body Assembly`)—only the plate beneath them.
4. **Serviceability:** Must allow for installation and removal of the base plate and case walls without damage or interference.
5. **Clearance for Components:** Must allow adequate clearance beneath the base plate for connectors, wiring, or hardware.

## Physical & Manufacturing Requirements

1. **3D Printability:** Must be manufacturable as a single 3D-printed part on a print bed of at least 256x256mm.
2. **Material:** Recommended materials include PETG, ABS, or similar with sufficient structural rigidity.
3. **Dimensional Fit:** Must align with the base plate footprint and internal volume defined by the `77875 - Ghost Volume, Throttle Body`.

## Assembly & Hierarchy

1. **Parent Assembly:** Component of `62988 - HSI Mk.1 Mounting Kit`.
2. **Mounting Method:** Attaches between the **Base Plate** and the **case walls**, enabling enclosure use only.

## Naming and Clarification

* This part shall be referred to as the **Case Adapter**.
* It is **not** to be confused with the **Base Plate**, which directly supports the throttle hardware.
* It is **not** used in installations involving:
  - **DZUS rails**
  - **Standalone trays**
  - **Direct mounting to a cockpit panel or desktop**

## Exclusions

* Not used when the HSI Mk.1 throttle is mounted using DZUS rails.
* Not used when mounted to a standalone tray or open frame.
* Not a substitute for the Base Plate or Body Assembly.

