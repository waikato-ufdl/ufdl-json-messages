from wai.json.object import JSONObject
from wai.json.object.property import StringProperty, BoolProperty


class FinishJobSpec(JSONObject['FinishJobSpec']):
    """
    Specifies the JSON data structure required to
    finish a job.
    """
    # Whether the job was successful
    success: bool = BoolProperty()

    # The type of notification to send
    send_notification: str = StringProperty()

    # Any error that occurred while running the job
    error: str = StringProperty(optional=True)
