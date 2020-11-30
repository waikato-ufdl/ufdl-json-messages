from typing import Dict

from wai.json.object import StrictJSONObject
from wai.json.object.property import StringProperty, MapProperty

from ._ValueTypePair import ValueTypePair


class CreateJobSpec(StrictJSONObject['CreateJobSpec']):
    """
    Specifies the JSON data structure for specifying the arguments
    to execute a job-template with.
    """
    # The values of the inputs
    input_values: Dict[str, ValueTypePair] = MapProperty(
        value_property=ValueTypePair.as_property()
    )

    # The values of the parameters
    parameter_values: Dict[str, str] = MapProperty(
        value_property=StringProperty(),
        optional=True
    )

    # A description of the job
    description: str = StringProperty(optional=True, default="")
