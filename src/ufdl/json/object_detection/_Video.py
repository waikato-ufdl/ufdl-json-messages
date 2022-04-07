from typing import List

from wai.json.object.property import ArrayProperty, NumberProperty

from ._File import File
from ._VideoAnnotation import VideoAnnotation


class Video(File['Video']):
    """
    Represents a single video and its annotations.
    """
    # The length (in seconds) of the video
    length: float = NumberProperty(minimum=0.0)

    # The annotations of the image
    annotations: List[VideoAnnotation] = ArrayProperty(
        element_property=VideoAnnotation.as_property()
    )
