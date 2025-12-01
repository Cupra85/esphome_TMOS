# esphome_TMOS

ESPHome driver for the STMicroelectronics STHS34PF80 TMOS thermal IR presence sensor.

## Features
- Presence detection
- Motion detection
- Thermal shock detection
- Ambient temperature (°C)
- Object temperature (°C)
- Auto-detects I²C address (0x5A or 0x5B)
- Full debug logging

## I²C Address
The STHS34PF80 uses:

- 0x5A when SA0 = GND  
- 0x5B when SA0 = VCC  

This driver automatically detects both.

## Register Map

| Function | Register | Size |
|----------|----------|------|
| Ambient Temperature | 0x0C | 16-bit |
| Object Temperature | 0x0E | 16-bit |
| Presence | 0x15 | 8-bit |
| Motion | 0x16 | 8-bit |
| Thermal Shock | 0x17 | 8-bit |
| Control | 0x20 | 8-bit |

## Example ESPHome YAML

```yaml
external_components:
  - source:
      type: local
      path: esphome_TMOS/components

i2c:
  sda: 8
  scl: 9
  scan: true

sensor:
  - platform: tmos
    ambient_temperature:
      name: "TMOS Ambient Temperature"
    object_temperature:
      name: "TMOS Object Temperature"

binary_sensor:
  - platform: tmos
    presence:
      name: "TMOS Presence"
    motion:
      name: "TMOS Motion"
    thermal_shock:
      name: "TMOS Thermal Shock"
