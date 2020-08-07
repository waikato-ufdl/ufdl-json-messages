from wai.json.object import StrictJSONObject
from wai.json.object.property import StringProperty


class JobOutputTypeSpec(StrictJSONObject['JobOutputTypeSpec']):
    """
    Specifies the JSON data structure for specifying the type
    of a job output.
    """
    # The type of the output
    type: str = StringProperty(max_length=64)
