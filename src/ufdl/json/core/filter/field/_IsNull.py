from wai.json.object.property import ConstantProperty

from ._FieldFilterExpression import FieldFilterExpression


class IsNull(FieldFilterExpression['IsNull']):
    """
    Filter expression which filters the list to those entries
    where the value in the specified field is null.
    """
    # Keyword identifying this object as an 'isnull' expression
    type: str = ConstantProperty(value="isnull")

    def __init__(self, **initial_values):
        # Automatically supply the type argument
        initial_values.setdefault("type", "isnull")

        super().__init__(**initial_values)
