from wai.json.object import StrictJSONObject
from wai.json.object.property import StringProperty


class Transcription(StrictJSONObject['Transcription']):
    """
    The transcription of a single speech audio-file.
    """
    # The text of the transcription itself
    transcription = StringProperty(optional=True, default="")
