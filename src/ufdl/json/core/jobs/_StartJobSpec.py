from wai.json.object import JSONObject
from wai.json.object.property import StringProperty


class StartJobSpec(JSONObject['StartJobSpec']):
    """
    Specifies the JSON data structure required to
    start a job.
    """
    # The type of notification to send
    send_notification: str = StringProperty()
