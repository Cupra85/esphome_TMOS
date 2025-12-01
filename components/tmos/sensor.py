import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, binary_sensor, i2c

TMOS_NS = cg.esphome_ns.namespace("TMOS")
TMOSComponent = TMOS_NS.class_("TMOSComponent", cg.PollingComponent, i2c.I2CDevice)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(TMOSComponent),

    cv.Optional("ambient_temperature"): sensor.sensor_schema(),
    cv.Optional("object_temperature"): sensor.sensor_schema(),

    cv.Optional("presence"): binary_sensor.binary_sensor_schema(),
    cv.Optional("motion"): binary_sensor.binary_sensor_schema(),
    cv.Optional("thermal_shock"): binary_sensor.binary_sensor_schema(),
}).extend(i2c.i2c_device_schema(None))  # address auto-detected

async def to_code(config):
    comp = cg.new_Pvariable(config["id"])
    await cg.register_component(comp, {})
    await i2c.register_i2c_device(comp, config)

    if "ambient_temperature" in config:
        s = await sensor.new_sensor(config["ambient_temperature"])
        cg.add(comp.set_ambient_temperature_sensor(s))

    if "object_temperature" in config:
        s = await sensor.new_sensor(config["object_temperature"])
        cg.add(comp.set_object_temperature_sensor(s))

    if "presence" in config:
        bs = await binary_sensor.new_binary_sensor(config["presence"])
        cg.add(comp.set_presence_sensor(bs))

    if "motion" in config:
        bs = await binary_sensor.new_binary_sensor(config["motion"])
        cg.add(comp.set_motion_sensor(bs))

    if "thermal_shock" in config:
        bs = await binary_sensor.new_binary_sensor(config["thermal_shock"])
        cg.add(comp.set_thermal_shock_sensor(bs))
