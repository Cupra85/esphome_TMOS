#pragma once
#include "esphome.h"

class TMOSComponent : public esphome::PollingComponent, public esphome::i2c::I2CDevice {
 public:
  TMOSComponent() : PollingComponent(500) {}

  void setup() override;
  void update() override;

  void set_ambient_temperature_sensor(esphome::sensor::Sensor *s) { ambient_temp_ = s; }
  void set_object_temperature_sensor(esphome::sensor::Sensor *s) { object_temp_ = s; }
  void set_presence_sensor(esphome::binary_sensor::BinarySensor *b) { presence_ = b; }
  void set_motion_sensor(esphome::binary_sensor::BinarySensor *b) { motion_ = b; }
  void set_thermal_shock_sensor(esphome::binary_sensor::BinarySensor *b) { shock_ = b; }

 protected:
  uint8_t i2c_addr_ = 0x5A;

  esphome::sensor::Sensor *ambient_temp_{nullptr};
  esphome::sensor::Sensor *object_temp_{nullptr};
  esphome::binary_sensor::BinarySensor *presence_{nullptr};
  esphome::binary_sensor::BinarySensor *motion_{nullptr};
  esphome::binary_sensor::BinarySensor *shock_{nullptr};

  int16_t read16(uint8_t reg);
  uint8_t read8(uint8_t reg);
};
