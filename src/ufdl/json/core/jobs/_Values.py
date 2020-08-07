from wai.json.object import JSONObject
from wai.json.object.property import StringProperty


class Values(JSONObject['Values']):
    """
    Specifies the JSON data structure for specifying the values
    to the inputs/parameters of a job template.
    """
    @classmethod
    def _additional_properties_validation(cls) -> StringProperty:
        return StringProperty(optional=True)
