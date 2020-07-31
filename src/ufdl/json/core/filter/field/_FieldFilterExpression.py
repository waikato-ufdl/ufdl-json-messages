from abc import ABC
from typing import TypeVar

from wai.json.object.property import StringProperty

from .._FilterExpression import FilterExpression

SelfType = TypeVar("SelfType", bound='FieldFilterExpression')


class FieldFilterExpression(FilterExpression[SelfType], ABC):
    """
    Base class for filter expressions which operate on a
    particular field of a model.
    """
    # The field on which to operate
    field: str = StringProperty(
        min_length=1
    )

    def __and__(self, other):
        from ..logical import And

        if isinstance(other, And):
            return And(sub_expressions=[self] + other.sub_expressions)
        elif isinstance(other, FieldFilterExpression):
            return And(sub_expressions=[self, other])
        else:
            raise TypeError(f"Can't perform logical and between "
                            f"{self.__class__.__name__} and {other.__class__.__name__}")

    def __or__(self, other):
        from ..logical import Or, And

        if isinstance(other, Or):
            return Or(sub_expressions=[self] + other.sub_expressions)
        elif isinstance(other, (And, FieldFilterExpression)):
            return Or(sub_expressions=[self, other])
        else:
            raise TypeError(f"Can't perform logical or between "
                            f"{self.__class__.__name__} and {other.__class__.__name__}")

