from typing import List

from wai.json.object.property import ArrayProperty

from ._File import File
from ._ImageAnnotation import ImageAnnotation


class Image(File['Image']):
    """
    Represents a single image and its annotations.
    """
    # The annotations of the image
    annotations: List[ImageAnnotation] = ArrayProperty(
        element_property=ImageAnnotation.as_property()
    )
