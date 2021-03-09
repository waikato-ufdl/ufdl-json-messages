from typing import List, Union

from wai.json.object import StrictJSONObject
from wai.json.object.property import ArrayProperty, OneOfProperty

from ._EmailNotification import EmailNotification
from ._PrintNotification import PrintNotification
from ._WebSocketNotification import WebSocketNotification

# The different types of notification that UFDL supports
NotificationTypes = (
    EmailNotification,
    PrintNotification,
    WebSocketNotification
)

# The union of the types of notification UFDL supports
NotificationUnionType = Union[EmailNotification, PrintNotification, WebSocketNotification]


def _create_notification_array_property() -> ArrayProperty:
    """
    Creates a property which holds an array of notification types.

    :return:
                The array property.
    """
    return ArrayProperty(
        element_property=OneOfProperty(
            sub_properties=tuple(
                NotificationType.as_property()
                for NotificationType in NotificationTypes
            )
        ),
        optional=True,
        default=[]
    )


class NotificationActions(StrictJSONObject['NotificationActions']):
    """
    Specification of the notifications that a job should send at various
    stages in its lifecycle.
    """
    # The notifications to send when a job is acquired
    on_acquire: List[NotificationUnionType] = _create_notification_array_property()

    # The notifications to send when a job is released
    on_release: List[NotificationUnionType] = _create_notification_array_property()

    # The notifications to send when a job is started
    on_start: List[NotificationUnionType] = _create_notification_array_property()

    # The notifications to send when a job is finished
    on_finish: List[NotificationUnionType] = _create_notification_array_property()

    # The notifications to send when a job is finished in error
    on_error: List[NotificationUnionType] = _create_notification_array_property()

    # The notifications to send when a job is reset
    on_reset: List[NotificationUnionType] = _create_notification_array_property()

    # The notifications to send when a job is aborted
    on_abort: List[NotificationUnionType] = _create_notification_array_property()
