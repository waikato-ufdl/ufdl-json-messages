from typing import List

from wai.json.object import StrictJSONObject
from wai.json.object.property import StringProperty, ArrayProperty


class InputSpec(StrictJSONObject['InputSpec']):
    """
    Specifies the JSON data structure for specifying the type
    and options to an input to a job template.
    """
    # The name of the input
    name: str = StringProperty(min_length=1)

    # The possible types of value the input expects
    types: List[str] = ArrayProperty(
        element_property=StringProperty(min_length=1),
        min_elements=1
    )

    # The options to the input
    options: str = StringProperty(optional=True, default="")

    # The help text for the input
    help: str = StringProperty(optional=True, default="")
