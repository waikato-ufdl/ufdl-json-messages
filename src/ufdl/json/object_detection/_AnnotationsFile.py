from wai.json.object import JSONObject
from wai.json.object.property import OneOfProperty

from ._Image import Image
from ._Video import Video


class AnnotationsFile(JSONObject['AnnotationsFile']):
    """
    Defines the annotations for images/videos in a dataset.
    """
    @classmethod
    def _additional_properties_validation(cls) -> OneOfProperty:
        return OneOfProperty(
            sub_properties=(
                Image.as_property(),
                Video.as_property()
            ),
            optional=True
        )
