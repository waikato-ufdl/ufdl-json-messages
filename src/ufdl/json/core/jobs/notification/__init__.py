"""
JSON specifications of different types of notifications that jobs
can send when they make phase transitions.
"""
from ._EmailNotification import EmailNotification
from ._Notification import Notification
from ._NotificationActions import NotificationActions, NotificationTypes, NotificationUnionType
from ._NotificationOverride import NotificationOverride
from ._PrintNotification import PrintNotification
from ._WebSocketNotification import WebSocketNotification
