from typing import Union

from wai.json.object.property import (
    StringProperty,
    ConstantProperty,
    OneOfProperty,
    NumberProperty,
    EnumProperty
)

from ._FieldFilterExpression import FieldFilterExpression


class Compare(FieldFilterExpression['Compare']):
    """
    Filter expression which filters the list to those entries
    whose field compares to a given value (e.g. >, <, >=, <=).
    """
    # Keyword identifying this object as a 'compare' expression
    type: str = ConstantProperty(value="compare")

    # The type of comparison to perform
    operator: str = EnumProperty(values=("<", ">", ">=", "<="))

    # The value to compare to
    value: Union[str, int, float] = OneOfProperty(
        sub_properties=(
            StringProperty(),
            NumberProperty()
        )
    )

    def __init__(self, **initial_values):
        # Automatically supply the type argument
        initial_values.setdefault("type", "compare")

        super().__init__(**initial_values)
