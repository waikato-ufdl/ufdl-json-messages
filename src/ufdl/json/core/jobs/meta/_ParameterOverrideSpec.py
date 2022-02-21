from wai.common.meta import instanceoptionalmethod
from wai.json.object import StrictJSONObject
from wai.json.object.property import RawProperty, StringProperty, BoolProperty
from wai.json.raw import RawJSONElement
from wai.json.schema import IS_JSON_SCHEMA


class ParameterOverrideSpec(StrictJSONObject['ParameterOverrideSpec']):
    """
    Specifies the JSON data structure for specifying an override of
    the default/const settings for a parameter.
    """
    # An optional default value for the parameter
    default: RawJSONElement = RawProperty(schema=IS_JSON_SCHEMA, optional=True)

    # The type of the default value (if omitted, the first type in 'types' is used)
    default_type: str = StringProperty(optional=True)

    # Whether this parameter can be changed (requires a default if true)
    const: bool = BoolProperty(optional=True, default=False)

    @instanceoptionalmethod
    def _perform_special_json_validation(self, raw_json: RawJSONElement):
        # If const is set, so must be default
        if raw_json.get('const', False):
            if 'default' not in raw_json:
                raise Exception("Must provide a default value for const parameters")
