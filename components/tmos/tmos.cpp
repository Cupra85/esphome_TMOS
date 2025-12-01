#include "tmos.h"

#define REG_AMBIENT_TEMP  0x0C
#define REG_OBJECT_TEMP   0x0E
#define REG_PRESENCE      0x15
#define REG_MOTION        0x16
#define REG_SHOCK         0x17
#define REG_CTRL          0x20

void TMOSComponent::setup() {
  write_byte(REG_CTRL, 0x01);
}

int16_t TMOSComponent::read16(uint8_t reg) {
  uint8_t d[2];
  if (read_bytes(reg, d, 2) != esphome::i2c::ERROR_OK) return 0;
  return (int16_t)((d[1] << 8) | d[0]);
}

uint8_t TMOSComponent::read8(uint8_t reg) {
  uint8_t d = 0;
  read_byte(reg, &d);
  return d;
}

void TMOSComponent::update() {
  if (ambient_temp_) ambient_temp_->publish_state(read16(REG_AMBIENT_TEMP) / 100.0f);
  if (object_temp_) object_temp_->publish_state(read16(REG_OBJECT_TEMP) / 100.0f);
  if (presence_) presence_->publish_state(read8(REG_PRESENCE) > 0);
  if (motion_) motion_->publish_state(read8(REG_MOTION) > 0);
  if (shock_) shock_->publish_state(read8(REG_SHOCK) > 0);
}
