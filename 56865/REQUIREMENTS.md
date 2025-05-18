# Requirements for 56865 - Toggle Switch, 2 Position

This document outlines the key design and functional requirements for the Toggle Switch (Part Number 56865).

## Functional Requirements

1. **Switch Type:** 2-position maintained toggle switch
2. **Electrical Specifications:**
   * Configuration: SPST-NO (Single Pole, Single Throw, Normally Open)
   * Current Rating: 6A minimum
   * Number of Terminals: 2

3. **Function-Specific Requirements:**
   * **When Used for Manual Fuel Control:**
     * 2-Position Lever Lock Toggle
     * Release Force: 3-6 lb
     * Operating Force: 8 lb maximum
     * Actuation Angle: 21.5° ± 0.06°

   * **When Used for Jet Pipe Temp Limit (JPTL):**
     * 2-Position Toggle Switch
     * Operating Force: 28 oz + 8 oz (36 oz maximum)
     * Actuation Angle: 16° ± 1°

## Physical & Manufacturing Requirements

1. **Form Factor:** Round toggle
2. **Material:** Per manufacturer specification, suitable for cockpit environment
3. **Mounting:** Panel mount compatible with standard cockpit panel thickness
4. **Durability:** Must withstand repeated actuations without degradation of performance

## Interfacing Requirements

1. **Electrical Connection:** Compatible with standard aircraft electrical systems
2. **Panel Integration:** Must conform to standard panel cutout dimensions
3. **Terminal Accessibility:** Terminals must be accessible for secure wire connection

## Environmental Requirements

1. **Operating Temperature Range:** Suitable for cockpit environment (-20°C to +70°C)
2. **Humidity Resistance:** Capable of operation in varying humidity conditions

## Alternatives & Sourcing

1. **Commercial Alternative:** 
   * McMaster-Carr 7343K184 or Digikey TA2-1A-DC-5 
   * These parts are interchangeable for both functions

2. **MIL-SPEC Alternatives:** 
   * For Jet Pipe Temp Limit (JPTL): MS24523-22
   * For Manual Fuel Control: MS24658-22G
   * Note: MIL-SPEC parts are not interchangeable between functions

## Assembly & Hierarchy

1. **Parent Assembly:** This part is a component of `51364 - Sensors Kit`
2. **Quantity per Assembly:** 2 units (one for Manual Fuel Control, one for JPTL)

## Compliance

1. **Standards:** Should meet or exceed the requirements from the Air Crew Stations specification document
2. **Ergonomic Performance:** Operating forces and actuation angles must match specifications to provide authentic simulator control feel
