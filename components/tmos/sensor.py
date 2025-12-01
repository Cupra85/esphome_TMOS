import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, i2c

TMOS_NS = cg.esphome_ns.namespace("TMOS")
TMOSComponent = TMOS_NS.class_("TMOSComponent", cg.PollingComponent, i2c.I2CDevice)

TMOS_SENSOR_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(TMOSComponent),
    cv.Required("ambient_temperature"): sensor.sensor_schema(),
    cv.Required("object_temperature"): sensor.sensor_schema(),
}).extend(i2c.i2c_device_schema(0x5A))


async def to_code(config):
    var = cg.new_Pvariable(config["id"])
    await cg.register_component(var, {})
    await i2c.register_i2c_device(var, config)

    ambient = await sensor.new_sensor(config["ambient_temperature"])
    cg.add(var.set_ambient_temperature_sensor(ambient))

    object_temp = await sensor.new_sensor(config["object_temperature"])
    cg.add(var.set_object_temperature_sensor(object_temp))


# REGISTER PLATFORM
sensor.register_sensor_platform("tmos", TMOS_SENSOR_SCHEMA, to_code)
