from wai.json.object.property import StringProperty, BoolProperty, ConstantProperty

from ._FieldFilterExpression import FieldFilterExpression


class Contains(FieldFilterExpression['Contains']):
    """
    Filter expression which filters the list to those entries
    whose field contains some sub-string.
    """
    # Keyword identifying this object as a 'contains' expression
    type: str = ConstantProperty(value="contains")

    # The sub-string to filter for
    sub_string: str = StringProperty(
        min_length=1
    )

    # Whether the filtering should be performed without regard to case
    case_insensitive: bool = BoolProperty(
        optional=True,
        default=False
    )

    def __init__(self, **initial_values):
        # Automatically supply the type argument
        initial_values.setdefault("type", "contains")

        super().__init__(**initial_values)
