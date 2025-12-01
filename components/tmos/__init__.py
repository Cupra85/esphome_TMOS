
import esphome.config_validation as cv
from esphome.components import sensor as sensor_platform
from esphome.components import binary_sensor as binary_sensor_platform

from .sensor import (
    TMOS_SENSOR_SCHEMA,
    TMOS_BINARY_SCHEMA,
    to_code_sensor,
    to_code_binary,
)

# register both platforms under the name "tmos"
sensor_platform.register_sensor_platform("tmos", TMOS_SENSOR_SCHEMA, to_code_sensor)
binary_sensor_platform.register_binary_sensor_platform(
    "tmos", TMOS_BINARY_SCHEMA, to_code_binary
)
