from wai.json.object import JSONObject
from wai.json.object.property import JSONObjectProperty

from ._Transcription import Transcription


class TranscriptionsFile(JSONObject['TranscriptionsFile']):
    """
    Definition of a basic JSON file which holds a map
    from audio file names to their transcriptions.
    """
    @classmethod
    def _additional_properties_validation(cls) -> JSONObjectProperty:
        return Transcription.as_property(optional=True)
