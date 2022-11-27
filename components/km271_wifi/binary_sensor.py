import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor
from esphome.core import EnumValue

from esphome.const import (
    CONF_ID,
    DEVICE_CLASS_PROBLEM,
    DEVICE_CLASS_RUNNING,
)

from . import (
    CONF_KM271_ID,
    KM271
)

CODEOWNERS = ["@the78mole", "@jensgraef"]

TYPES = [
    "boiler_error",
    "boiler_running",
    "load_pump_running"
]

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(CONF_KM271_ID): cv.use_id(KM271),
            cv.Optional("boiler_error"): binary_sensor.binary_sensor_schema(
                device_class=DEVICE_CLASS_PROBLEM,
            ),
            cv.Optional("boiler_running"): binary_sensor.binary_sensor_schema(
                device_class=DEVICE_CLASS_RUNNING
            ),
            cv.Optional("load_pump_running"): binary_sensor.binary_sensor_schema(
                device_class=DEVICE_CLASS_RUNNING
            ),
        }
    )
)


async def setup_conf(config, key, hub):
    if key in config:
        conf = config[key]

        sens = await binary_sensor.new_binary_sensor(conf)
        cg.add(getattr(hub, f"set_{key}_binary_sensor")(sens))


async def to_code(config):
    hub = await cg.get_variable(config[CONF_KM271_ID])
    for key in TYPES:
        await setup_conf(config, key, hub)