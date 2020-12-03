from wai.json.object import StrictJSONObject
from wai.json.object.property import BoolProperty

from ._NotificationActions import NotificationActions


class NotificationOverride(StrictJSONObject['NotificationOverride']):
    """
    JSON specification of how to override the default job notifications.
    """
    # The actions to use to override the defaults
    actions: NotificationActions = NotificationActions.as_property()

    # Whether to keep the default actions as well
    keep_default: bool = BoolProperty(optional=True, default=False)
