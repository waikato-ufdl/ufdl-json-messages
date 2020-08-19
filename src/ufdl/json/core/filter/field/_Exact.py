from typing import Union

from wai.json.object.property import (
    StringProperty,
    BoolProperty,
    ConstantProperty,
    OneOfProperty,
    NumberProperty
)

from ._FieldFilterExpression import FieldFilterExpression


class Exact(FieldFilterExpression['Exact']):
    """
    Filter expression which filters the list to those entries
    whose field exactly matches some value.
    """
    # Keyword identifying this object as an 'exact' expression
    type: str = ConstantProperty(value="exact")

    # The value to match exactly
    value: Union[str, int, float, bool] = OneOfProperty(
        sub_properties=(
            StringProperty(),
            NumberProperty(),
            BoolProperty()
        )
    )

    # Whether the filtering should be performed without regard to case
    case_insensitive: bool = BoolProperty(
        optional=True,
        default=False
    )

    def __init__(self, **initial_values):
        # Automatically supply the type argument
        initial_values.setdefault("type", "exact")

        super().__init__(**initial_values)
