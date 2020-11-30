from wai.json.object import StrictJSONObject
from wai.json.object.property import StringProperty


class ValueTypePair(StrictJSONObject['ValueTypePair']):
    """
    A pair of a value and its type.
    """
    # The value passed to the input
    value: str = StringProperty()

    # The type of the value
    type: str = StringProperty()