from typing import TypeVar

from wai.json.object import StrictJSONObject
from wai.json.object.property import BoolProperty

SelfType = TypeVar("SelfType", bound='Notification')


class Notification(StrictJSONObject[SelfType]):
    """
    Base class for notification specifications.
    """
    # Whether this notification should be suppressed if the job is
    # part of a workflow
    suppress_for_parent: bool = BoolProperty(optional=True, default=True)
