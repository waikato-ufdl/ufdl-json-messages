from abc import ABC
from typing import TypeVar

from wai.json.object import StrictJSONObject
from wai.json.object.property import BoolProperty

SelfType = TypeVar("SelfType", bound='FilterExpression')


class FilterExpression(StrictJSONObject[SelfType], ABC):
    """
    Base class for expressions which filter a list request
    under some conditions.
    """
    # Whether to negate the filter conditions
    invert: bool = BoolProperty(
        optional=True,
        default=False
    )

    def __invert__(self):
        copy = self.json_copy()
        copy.invert = not self.invert
        return copy
