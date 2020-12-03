from wai.json.object.property import StringProperty

from ._Notification import Notification


class PrintNotification(Notification['PrintNotification']):
    """
    Notification specification for printing to standard output.
    """
    # The message to print
    message: str = StringProperty()
