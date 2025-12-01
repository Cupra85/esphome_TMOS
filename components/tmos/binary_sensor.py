import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor, i2c

TMOS_NS = cg.esphome_ns.namespace("TMOS")
TMOSComponent = TMOS_NS.class_("TMOSComponent", cg.PollingComponent, i2c.I2CDevice)

TMOS_BINARY_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(TMOSComponent),
    cv.Optional("presence"): binary_sensor.binary_sensor_schema(),
    cv.Optional("motion"): binary_sensor.binary_sensor_schema(),
    cv.Optional("thermal_shock"): binary_sensor.binary_sensor_schema(),
}).extend(i2c.i2c_device_schema(0x5A))


async def to_code(config):
    var = cg.new_Pvariable(config["id"])
    await cg.register_component(var, {})
    await i2c.register_i2c_device(var, config)

    if "presence" in config:
        bs = await binary_sensor.new_binary_sensor(config["presence"])
        cg.add(var.set_presence_sensor(bs))

    if "motion" in config:
        bs = await binary_sensor.new_binary_sensor(config["motion"])
        cg.add(var.set_motion_sensor(bs))

    if "thermal_shock" in config:
        bs = await binary_sensor.new_binary_sensor(config["thermal_shock"])
        cg.add(var.set_thermal_shock_sensor(bs))


# REGISTER PLATFORM
binary_sensor.register_binary_sensor_platform("tmos", TMOS_BINARY_SCHEMA, to_code)
