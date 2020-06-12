from wai.json.object import StrictJSONObject
from wai.json.object.property import StringProperty


class FileMetadata(StrictJSONObject['FileMetadata']):
    """
    JSON object containing the meta-data for a file.
    """
    # The meta-data
    metadata = StringProperty()
