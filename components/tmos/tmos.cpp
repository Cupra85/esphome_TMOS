#include "tmos.h"

#define REG_AMBIENT_TEMP  0x0C
#define REG_OBJECT_TEMP   0x0E
#define REG_PRESENCE      0x15
#define REG_MOTION        0x16
#define REG_SHOCK         0x17
#define REG_CTRL          0x20

void TMOSComponent::setup() {
  // Auto-detect address
  uint8_t dummy;
  if (read_byte(REG_CTRL, &dummy) != esphome::i2c::ERROR_OK) {
    this->set_address(0x5B);
    if (read_byte(REG_CTRL, &dummy) != esphome::i2c::ERROR_OK) {
      ESP_LOGE("TMOS", "Sensor not detected at 0x5A or 0x5B");
      return;
    }
    i2c_addr_ = 0x5B;
  }
  ESP_LOGI("TMOS", "Sensor found at I2C address 0x%02X", i2c_addr_);

  write_byte(REG_CTRL, 0x01);  // enable
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
  float amb = read16(REG_AMBIENT_TEMP) / 100.0f;
  float obj = read16(REG_OBJECT_TEMP) / 100.0f;
  bool p = read8(REG_PRESENCE) > 0;
  bool m = read8(REG_MOTION) > 0;
  bool s = read8(REG_SHOCK) > 0;

  if (ambient_temp_) ambient_temp_->publish_state(amb);
  if (object_temp_) object_temp_->publish_state(obj);
  if (presence_) presence_->publish_state(p);
  if (motion_) motion_->publish_state(m);
  if (shock_) shock_->publish_state(s);

  ESP_LOGI("TMOS", "Ambient=%.2f Object=%.2f Presence=%d Motion=%d Shock=%d",
           amb, obj, p, m, s);
}
