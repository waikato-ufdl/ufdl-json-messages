from wai.json.object import StrictJSONObject
from wai.json.object.property import StringProperty, RawProperty
from wai.json.raw import RawJSONElement
from wai.json.schema import IS_JSON_DEFINITION, IS_JSON_SCHEMA, JSONSchema
from wai.json.schema.constants import DEFINITIONS_KEYWORD

# A schema which accepts any valid JSON value
DEFAULT_SCHEMA: JSONSchema = {DEFINITIONS_KEYWORD: IS_JSON_DEFINITION}
DEFAULT_SCHEMA.update(IS_JSON_SCHEMA)


class ValueTypePair(StrictJSONObject['ValueTypePair']):
    """
    A pair of a value and its type.
    """
    # The value passed to the input
    value: RawJSONElement = RawProperty(schema=DEFAULT_SCHEMA)

    # The type of the value
    type: str = StringProperty()
