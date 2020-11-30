from wai.json.object import StrictJSONObject
from wai.json.object.property import StringProperty


class ParameterSpec(StrictJSONObject['ParameterSpec']):
    """
    Specifies the JSON data structure for specifying the type
    and default value to a parameter to a job template.
    """
    # The name of the parameter
    name: str = StringProperty(min_length=1, max_length=32)

    # The type of the parameter
    type: str = StringProperty(min_length=1, max_length=32)

    # The options to the parameter
    default: str = StringProperty(optional=True, default="")

    # The help text for the parameter
    help: str = StringProperty(optional=True, default="")
