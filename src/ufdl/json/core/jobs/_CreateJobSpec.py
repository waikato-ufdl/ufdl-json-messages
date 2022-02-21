from typing import Dict

from wai.json.object import StrictJSONObject
from wai.json.object.property import StringProperty, MapProperty

from .notification import NotificationOverride
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
    parameter_values: Dict[str, ValueTypePair] = MapProperty(
        value_property=ValueTypePair.as_property(),
        optional=True
    )

    # A description of the job
    description: str = StringProperty(optional=True, default="")

    # The notification override for the top-level job
    notification_override: NotificationOverride = NotificationOverride.as_property(optional=True)

    # The notification overrides for child-jobs
    child_notification_overrides: Dict[str, NotificationOverride] = MapProperty(
        value_property=NotificationOverride.as_property(),
        optional=True
    )
