# Requirements for 42807 - Mounting Tray

This document outlines the key design and functional requirements for the Mounting Tray (Part Number 42807).

## Functional Requirements

1.  **Facia Panel Mounting:** Shall serve as the primary mounting structure for all three facia panels.
2.  **Attachment Point Accuracy:** Panel attachment points shall be located approximately as shown on the physical/reference panel.
3.  **Serviceability:** Must be designed for serviceability, allowing fasteners (e.g., for attached components) to be removed and replaced multiple times without damaging the tray. This includes the use of heat-set inserts where appropriate.
4.  **Component Integration:** Shall provide a rigid structural interface for mounting the following components:
    *   Throttle assembly
    *   Nozzle control assembly
    *   Nozzle stop mechanism
    *   Parking brake mechanism
    *   Controller electronics
    *   Friction assemblies (if installed)
5.  **Rigidity:** Must provide a rigid fixture for the facia plates, associated linkages, and either Dzus rails or an external case as required.

## Physical & Manufacturing Requirements

1.  **3D Printability:** Must be manufacturable as a single piece via 3D printing on a print bed with dimensions of at least 256x256mm.
2.  **Dimensional Constraints:** When no external case is fitted, the tray must fit within the predefined rail geometry specified by part `77875 - Ghost Volume, Throttle Body`.

## Assembly & Hierarchy

1.  **Parent Assembly:** This part is a component of `96784 - Body Assembly`.
