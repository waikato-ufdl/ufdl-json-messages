from wai.json.object import StrictJSONObject
from wai.json.object.property import StringProperty

from .._ValueTypePair import ValueTypePair


class Dependency(StrictJSONObject['Dependency']):
    """
    A connection specifying that the input of a child job in a workflow should
    receive as input the output from another child job.
    """
    # The child node that will be expected to produce the output
    from_node: str = StringProperty()

    # The name and type of the output that will be expected
    from_output: ValueTypePair = ValueTypePair.as_property()

    # The child node that will receive the output's value as input
    to_node: str = StringProperty()

    # The input on the child node that will receive the value
    to_input: str = StringProperty()
