from wai.json.object.property import NumberProperty

from ._Annotation import Annotation
from ._ImageAnnotation import ImageAnnotation


class VideoAnnotation(Annotation['VideoAnnotation']):
    """
    Represents a single annotation in a video.
    """
    # The time into the video at which the detection occurred
    time: float = NumberProperty(minimum=0.0)

    @classmethod
    def from_image_annotation(
            cls,
            image_annotation: ImageAnnotation,
            time: float
    ) -> 'VideoAnnotation':
        return VideoAnnotation(
            time=time,
            **image_annotation.to_raw_json(validate=False)
        )

    def to_image_annotation(self) -> ImageAnnotation:
        args = self.to_raw_json(validate=False)
        del args['time']
        return ImageAnnotation(**args)
