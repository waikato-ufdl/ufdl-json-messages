from wai.json.object.property import NumberProperty

from ._File import File


class FileType(File['FileType']):
    """
    Message used to set the file-type of a file.
    """
    # The length (in seconds) of the video
    length: float = NumberProperty(minimum=0.0, optional=True)
