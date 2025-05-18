# Requirements for 23794 - Angle Sensor, Hall Effect

This document outlines the key design and functional requirements for the P3022 Hall Effect Angle Sensor (Part Number 23794).

## Functional Requirements

1. **Measurement Function:** Must provide precise, non-contact rotary position measurement for the throttle axes.
2. **Sensing Range:**
   * Primary Option (P3022C360V1T): 0-360° continuous rotation measurement
   * Alternative Option (P3022C90V1T): 0-90° limited rotation measurement
3. **Output Characteristics:**
   * Signal Type: Analog voltage output proportional to angle
   * Resolution: High precision, suitable for flight control input detection
   * Response Time: Fast enough for real-time flight simulator control input
4. **Electrical Specifications:**
   * Supply Voltage: Compatible with controller board (typically 5V DC)
   * Output Range: 0-5V proportional voltage output
   * Current Consumption: Low power consumption suitable for extended operation

## Physical & Manufacturing Requirements

1. **Form Factor:** Miniature size to fit within confined throttle mechanism spaces
2. **Mounting Interface:** 
   * Must be mechanically compatible with the HSI Mk.1 throttle axis mounting points
   * Installation must allow proper alignment with the rotation axes
3. **Dimensions:** As per P3022 series specifications
4. **Shaft/Magnet Interface:** Compatible with the throttle control axes

## Durability & Performance Requirements

1. **Lifespan:** Minimum 100,000 rotation cycles without calibration drift
2. **Mechanical Durability:** 
   * No-contact measurement to prevent mechanical wear
   * Shaft bearings (if applicable) must support smooth operation
3. **Temperature Range:** Suitable for indoor operation (0°C to 50°C minimum)
4. **Linearity:** High linearity across the measurement range

## Integration Requirements

1. **Electrical Interface:** Compatible with the HSI Mk.1 controller board
2. **Wiring:** Standardized connector or wire leads for integration with the `81137 - Wiring Harness`
3. **Calibration:** Easily calibratable in-situ 
4. **Mechanical Integration:**
   * Must be installable on all three measurement axes (throttle, nozzle position, and friction control)
   * Mounting orientation must be consistent with the sensor's measurement plane

## Usage Applications

These sensors will be installed in the following control axes:
1. Main throttle position measurement
2. Nozzle position control measurement
3. Possibly friction control or other auxiliary axis measurement

## Assembly & Hierarchy

1. **Parent Assembly:** This part is a component of `51364 - Sensors Kit`
2. **Quantity per Assembly:** 3 units (one per axis of measurement)
3. **Installation Sequence:** To be installed during final assembly of the respective control mechanisms

## Sourcing Options

1. **Primary Source:** CALT P3022C360V1T from manufacturer website (https://caltsensor.com/product/miniature-non-contact-angle-sensor-p3022-series/)
2. **Secondary Source:** Alternative supplier via Amazon (https://a.co/d/a8b02RU)
3. **Alternatives:** The P3022C90V1T may be substituted if the 360-degree measurement range is not required for a particular axis
