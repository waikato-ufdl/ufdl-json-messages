from typing import List, Optional, TypeVar

from wai.json.object import StrictJSONObject, Absent
from wai.json.object.property import ArrayProperty, StringProperty, NumberProperty

SelfType = TypeVar("SelfType", bound='File')


class File(StrictJSONObject[SelfType]):
    """
    Represents a single image and its annotations.
    """
    # The file's format
    format: str = StringProperty(optional=True)

    # The file's dimensions
    dimensions: List[int] = ArrayProperty(
        element_property=NumberProperty(integer_only=True, minimum=1),
        min_elements=2, max_elements=2,
        optional=True
    )

    @property
    def width(self) -> Optional[int]:
        """
        Gets the width from the dimensions.

        :return:    The width, or None if not available.
        """
        if self.dimensions is not Absent:
            return self.dimensions[0]

    @property
    def height(self) -> Optional[int]:
        """
        Gets the height from the dimensions.

        :return:    The height, or None if not available.
        """
        if self.dimensions is not Absent:
            return self.dimensions[1]
