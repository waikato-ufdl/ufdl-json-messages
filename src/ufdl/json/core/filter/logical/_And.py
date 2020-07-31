from typing import List, Union

from wai.json.object.property import ArrayProperty, OneOfProperty, ConstantProperty

from ..field import *
from .._FilterExpression import FilterExpression


class And(FilterExpression['And']):
    """
    Filter expression which is the logical and of a
    number of sub-expresssions.
    """
    # Keyword identifying this object as an 'and' expression
    type: str = ConstantProperty(value="and")

    # The sub-expressions of the logical and
    sub_expressions: List[FieldFilterExpression] = ArrayProperty(
        element_property=OneOfProperty(
            sub_properties=(
                Contains.as_property(),
                Exact.as_property()
            )
        ),
        min_elements=2
    )

    def __init__(self, **initial_values):
        # Automatically supply the type argument
        initial_values.setdefault("type", "and")

        super().__init__(**initial_values)

    def __and__(self, other):
        if isinstance(other, And):
            return And(sub_expressions=self.sub_expressions + other.sub_expressions)
        elif isinstance(other, FieldFilterExpression):
            return And(sub_expressions=self.sub_expressions + [other])
        else:
            raise TypeError(f"Can't perform logical and between "
                            f"{self.__class__.__name__} and {other.__class__.__name__}")
