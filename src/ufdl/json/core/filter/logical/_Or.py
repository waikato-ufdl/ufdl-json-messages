from typing import List, Union

from wai.json.object.property import ArrayProperty, OneOfProperty, ConstantProperty

from ..field import *
from .._FilterExpression import FilterExpression
from ._And import And


class Or(FilterExpression['Or']):
    """
    Filter expression which is the logical or of a
    number of sub-expresssions.
    """
    # Keyword identifying this object as an 'and' expression
    type: str = ConstantProperty(value="or")

    # The sub-expressions of the logical and
    sub_expressions: List[Union[And, FieldFilterExpression]] = ArrayProperty(
        element_property=OneOfProperty(
            sub_properties=(
                And.as_property(),
                *(field_filter_expression.as_property()
                  for field_filter_expression in ALL_FIELD_FILTER_EXPRESSIONS)
            )
        ),
        min_elements=2
    )

    def __init__(self, **initial_values):
        # Automatically supply the type argument
        initial_values.setdefault("type", "or")

        super().__init__(**initial_values)

    def __or__(self, other):
        if isinstance(other, Or):
            return Or(sub_expressions=self.sub_expressions + other.sub_expressions)
        elif isinstance(other, (And, FieldFilterExpression)):
            return Or(sub_expressions=self.sub_expressions + [other])
        else:
            raise TypeError(f"Can't perform logical or between "
                            f"{self.__class__.__name__} and {other.__class__.__name__}")
