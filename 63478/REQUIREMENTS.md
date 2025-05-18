# Requirements for 63478 - Toggle Switch, 3 Position

This document outlines the key design and functional requirements for the 3-Position Toggle Switch (Part Number 63478).

## Functional Requirements

1. **Switch Type:** 3-position momentary toggle switch
2. **Electrical Specifications:**
   * Configuration: DPDT (Double Pole, Double Throw)
   * Current Rating: 6A minimum
   * Voltage Rating: 28VDC
   * Number of Terminals: 6

3. **Function-Specific Requirements for Rudder Trim:**
   * Momentary return to center (spring-loaded)
   * Operating Force: 20-24 oz
   * Actuation Angle: 17° ± 1° each side from center position
   * Center detent force: 8-10 oz
   * Return-to-center spring force: Must return to center position when released from either extreme

## Physical & Manufacturing Requirements

1. **Form Factor:** Round toggle with IP67 rating
2. **Material:** Per manufacturer specification, suitable for cockpit environment
3. **Mounting:** Panel mount compatible with standard cockpit panel thickness (0.125" - 0.187")
4. **Durability:** Must withstand 100,000 actuations minimum without degradation of performance

## Interfacing Requirements

1. **Electrical Connection:** Solder lugs or quick-connect terminals
2. **Panel Integration:** 0.5" (12.7mm) mounting hole
3. **Terminal Accessibility:** Terminals must be accessible for secure wire connection
4. **Labeling:** Must accommodate NOSE UP/NOSE DOWN labeling on panel

## Environmental Requirements

1. **Operating Temperature Range:** -30°C to +85°C
2. **Humidity Resistance:** IP67 rated or equivalent
3. **Vibration Resistance:** Must maintain functionality under typical cockpit vibration conditions

## Alternatives & Sourcing

1. **Commercial Alternative:** 
   * McMaster-Carr 6D1-003
   * Digikey 3-position momentary toggle switch with DPDT configuration
   * These parts must be verified for correct return-to-center spring functionality

2. **MIL-SPEC Alternative:** 
   * MS24524-27
   * Note: This is the original specification part used in aircraft

## Assembly & Hierarchy

1. **Parent Assembly:** This part is a component of `51364 - Sensors Kit`
2. **Quantity per Assembly:** 1 unit (for Rudder Trim control)

## Compliance

1. **Standards:** Should meet or exceed the requirements from the Air Crew Stations specification document
2. **Ergonomic Performance:** Operating forces and actuation angles must match specifications to provide authentic simulator control feel
3. **Operational Feel:** Must provide positive tactile feedback when moved away from center position
