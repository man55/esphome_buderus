import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import select
from esphome.const import (
    CONF_ID,
    CONF_OPTIONS
)

from . import (
    CONF_KM271_ID,
    KM271
)

from .const import *

CODEOWNERS = ["@the78mole", "@jensgraef"]

TYPES = [

#    CONF_BLR_BUILDING_TYPE,
    CONF_HC1_SWT_SWITCH,
    CONF_HC1_HEATING_PROGRAM,
    CONF_HC1_OPMODE,
    CONF_HC1_LOWERING_TYPE,
    CONF_HC1_HEATINGS_TYPE,
    CONF_HC2_SWT_SWITCH,
    CONF_HC2_HEATING_PROGRAM,
    CONF_HC2_OPMODE,
    CONF_HC2_LOWERING_TYPE,
    CONF_HC2_HEATINGS_TYPE,
    CONF_WW_OPMODE,
    CONF_WW_CIRC_PUMP_INTERVALL,
]

km271_ns = cg.esphome_ns.namespace("KM271")

BuderusParamSelect = km271_ns.class_("BuderusParamSelect", select.Select, cg.Component)


# taken from tuya select
def ensure_option_map(value):
    cv.check_not_templatable(value)
    option = cv.All(cv.int_range(0, 2**8 - 1))
    mapping = cv.All(cv.string_strict)
    options_map_schema = cv.Schema({option: mapping})
    value = options_map_schema(value)

    all_values = list(value.keys())
    unique_values = set(value.keys())
    if len(all_values) != len(unique_values):
        raise cv.Invalid("Mapping values must be unique.")

    return value




CONFIG_SCHEMA = (
    cv.Schema(
        {
#            cv.GenerateID(CONF_KM271_ID): cv.use_id(KM271),
#            cv.Optional(CONF_BLR_BUILDING_TYPE): select.SELECT_SCHEMA.extend({
#                cv.GenerateID(): cv.declare_id(BuderusParamSelect),
#                cv.Optional(CONF_OPTIONS, default={0: 'Leicht', 1: 'Mittel', 2: 'Schwer'}): ensure_option_map
#            }),

            cv.GenerateID(CONF_KM271_ID): cv.use_id(KM271),
            cv.Optional(CONF_HC1_SWT_SWITCH): select.SELECT_SCHEMA.extend({
                cv.GenerateID(): cv.declare_id(BuderusParamSelect),
                cv.Optional(CONF_OPTIONS, default={9: 'Лето', 10: '10°C', 11: '11°C', 12: '12°C', 13: '13°C', 14: '14°C', 15: '15°C', 16: '16°C', 17: '17°C', 18: '18°C', 19: '19°C', 20: '20°C', 21: '21°C', 22: '22°C', 23: '23°C', 24: '24°C', 25: '25°C', 26: '26°C', 27: '27°C', 28: '28°C', 29: '29°C', 30: '30°C', 31: 'Зима'}): ensure_option_map
            }),
            cv.GenerateID(CONF_KM271_ID): cv.use_id(KM271),
            cv.Optional(CONF_HC1_HEATING_PROGRAM): select.SELECT_SCHEMA.extend({
                cv.GenerateID(): cv.declare_id(BuderusParamSelect),
                cv.Optional(CONF_OPTIONS, default={0: 'Собственная', 1: 'Семья', 2: 'Ранний', 3: 'Поздний', 4: 'Утро', 5: 'Полдень', 6: 'Обед', 7: 'Одинокий', 8: 'Ранний'}): ensure_option_map
            }),
            cv.GenerateID(CONF_KM271_ID): cv.use_id(KM271),
            cv.Optional(CONF_HC1_OPMODE): select.SELECT_SCHEMA.extend({
                cv.GenerateID(): cv.declare_id(BuderusParamSelect),
                cv.Optional(CONF_OPTIONS, default={0: 'Ночь', 1: 'День', 2: 'Авто'}): ensure_option_map
            }),
            cv.GenerateID(CONF_KM271_ID): cv.use_id(KM271),
            cv.Optional(CONF_HC1_LOWERING_TYPE): select.SELECT_SCHEMA.extend({
                cv.GenerateID(): cv.declare_id(BuderusParamSelect),
                cv.Optional(CONF_OPTIONS, default={0: 'Выкл', 1: 'Понижение', 2: 'Room hold', 3: 'Outside stop'}): ensure_option_map
            }),
            cv.GenerateID(CONF_KM271_ID): cv.use_id(KM271),
            cv.Optional(CONF_HC1_HEATINGS_TYPE): select.SELECT_SCHEMA.extend({
                cv.GenerateID(): cv.declare_id(BuderusParamSelect),
                cv.Optional(CONF_OPTIONS, default={0: 'Выкл', 1: 'Радиатор'}): ensure_option_map
            }),

            cv.GenerateID(CONF_KM271_ID): cv.use_id(KM271),
            cv.Optional(CONF_HC2_SWT_SWITCH): select.SELECT_SCHEMA.extend({
                cv.GenerateID(): cv.declare_id(BuderusParamSelect),
                cv.Optional(CONF_OPTIONS, default={9: 'Sommer', 10: '10°C', 11: '11°C', 12: '12°C', 13: '13°C', 14: '14°C', 15: '15°C', 16: '16°C', 17: '17°C', 18: '18°C', 19: '19°C', 20: '20°C', 21: '21°C', 22: '22°C', 23: '23°C', 24: '24°C', 25: '25°C', 26: '26°C', 27: '27°C', 28: '28°C', 29: '29°C', 30: '30°C', 31: 'Winter'}): ensure_option_map
            }),
            cv.GenerateID(CONF_KM271_ID): cv.use_id(KM271),
            cv.Optional(CONF_HC2_HEATING_PROGRAM): select.SELECT_SCHEMA.extend({
                cv.GenerateID(): cv.declare_id(BuderusParamSelect),
                cv.Optional(CONF_OPTIONS, default={0: 'Собственная', 1: 'Семья', 2: 'Ранний', 3: 'Поздний', 4: 'Утро', 5: 'Полдень', 6: 'Обед', 7: 'Одинокий', 8: 'Ранний'}): ensure_option_map
            }),
            cv.Optional(CONF_HC2_OPMODE): select.SELECT_SCHEMA.extend({
                cv.GenerateID(): cv.declare_id(BuderusParamSelect),
                cv.Optional(CONF_OPTIONS, default={0: 'Ночь', 1: 'День', 2: 'Авто'}): ensure_option_map
            }),
            cv.GenerateID(CONF_KM271_ID): cv.use_id(KM271),
            cv.Optional(CONF_HC2_LOWERING_TYPE): select.SELECT_SCHEMA.extend({
                cv.GenerateID(): cv.declare_id(BuderusParamSelect),
                cv.Optional(CONF_OPTIONS, default={0: 'Выкл', 1: 'Понижение', 2: 'Room hold', 3: 'Outside stop'}): ensure_option_map
            }),
            cv.GenerateID(CONF_KM271_ID): cv.use_id(KM271),
            cv.Optional(CONF_HC2_HEATINGS_TYPE): select.SELECT_SCHEMA.extend({
                cv.GenerateID(): cv.declare_id(BuderusParamSelect),
                cv.Optional(CONF_OPTIONS, default={0: 'Выкл', 1: 'Радиатор', 3: 'Пол'}): ensure_option_map
            }),

            cv.Optional(CONF_WW_OPMODE): select.SELECT_SCHEMA.extend({
                cv.GenerateID(): cv.declare_id(BuderusParamSelect),
                cv.Optional(CONF_OPTIONS, default={0: 'Выкл', 1: 'Вкл', 2: 'Авто'}): ensure_option_map
            }),
            cv.Optional(CONF_WW_CIRC_PUMP_INTERVALL): select.SELECT_SCHEMA.extend({
                cv.GenerateID(): cv.declare_id(BuderusParamSelect),
                cv.Optional(CONF_OPTIONS, default={0: 'Выкл', 1: '1 раз/ч', 2: '2 раза/ч', 3: '3 раза/ч', 4: '4 раза/ч', 5: '5 раза/ч', 6: '6 раза/ч', 7: 'Всегда вкл'}): ensure_option_map
            })

        }
    )
)


async def setup_conf(config, key, hub):
    if key in config:
        conf = config[key]
        options_map = conf[CONF_OPTIONS]
        sens = await select.new_select(conf, options=list(options_map.values()))
        cg.add(sens.setSelectMappings(list(options_map.keys())))
        cg.add(getattr(hub, f"set_communication_component")(cg.RawExpression("KM271::" + key), sens))


async def to_code(config):
    hub = await cg.get_variable(config[CONF_KM271_ID])
    for key in TYPES:
        await setup_conf(config, key, hub)
