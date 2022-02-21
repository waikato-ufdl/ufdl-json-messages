from typing import List

from wai.common.meta import instanceoptionalmethod
from wai.json.object import StrictJSONObject
from wai.json.object.property import RawProperty, StringProperty, ArrayProperty, BoolProperty
from wai.json.raw import RawJSONElement
from wai.json.schema import IS_JSON_DEFINITION, IS_JSON_SCHEMA, JSONSchema
from wai.json.schema.constants import DEFINITIONS_KEYWORD

# A schema which accepts any valid JSON value
DEFAULT_SCHEMA: JSONSchema = {DEFINITIONS_KEYWORD: IS_JSON_DEFINITION}
DEFAULT_SCHEMA.update(IS_JSON_SCHEMA)


class ParameterSpec(StrictJSONObject['ParameterSpec']):
    """
    Specifies the JSON data structure for specifying the type
    and default value to a parameter to a job template.
    """
    # The types of value that the parameter can take
    types: List[str] = ArrayProperty(
        element_property=StringProperty(min_length=1, max_length=256),
        min_elements=1
    )

    # An optional default value for the parameter
    default: RawJSONElement = RawProperty(schema=DEFAULT_SCHEMA, optional=True)

    # The type of the default value (if omitted, the first type in 'types' is used)
    default_type: str = StringProperty(optional=True)

    # Whether this parameter can be changed (requires a default if true)
    const: bool = BoolProperty(optional=True, default=False)

    # The help text for the parameter
    help: str = StringProperty()

    @instanceoptionalmethod
    def _perform_special_json_validation(self, raw_json: RawJSONElement):
        # If const is set, so must be default
        if raw_json.get('const', False):
            if 'default' not in raw_json:
                raise Exception("Must provide a default value for const parameters")
