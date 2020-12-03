from typing import List

from wai.json.object.property import StringProperty, ArrayProperty

from ._Notification import Notification


class EmailNotification(Notification['EmailNotification']):
    """
    Notification specification for sending an email.
    """
    # The subject of the email
    subject: str = StringProperty()

    # The body of the email
    body: str = StringProperty()

    # The recipients of the email (defaults to the job's creator if omitted)
    to: List[str] = ArrayProperty(
        element_property=StringProperty(),
        min_elements=1,
        unique_elements=True,
        optional=True
    )

    # Copied recipients of the email (defaults to no-one)
    cc: List[str] = ArrayProperty(
        element_property=StringProperty(),
        min_elements=1,
        unique_elements=True,
        optional=True
    )

    # Blind-copied recipients of the email (defaults to no-one)
    bcc: List[str] = ArrayProperty(
        element_property=StringProperty(),
        min_elements=1,
        unique_elements=True,
        optional=True
    )
