from wai.json.object import StrictJSONObject
from wai.json.object.property import StringProperty, BoolProperty


class InputSpec(StrictJSONObject['InputSpec']):
    """
    Specifies the JSON data structure for specifying the type
    and options to an input to a job template.
    """
    # The type of the input
    type: str = StringProperty(min_length=1, max_length=32)

    # The options to the input
    options: str = StringProperty()

    # The help text for the input
    help: str = StringProperty(optional=True)

    # Whether the input should be forwarded in a pipeline
    forward: bool = BoolProperty(optional=True, default=False)
