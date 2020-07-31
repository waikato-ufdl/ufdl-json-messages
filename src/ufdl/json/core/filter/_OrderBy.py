from wai.json.object import StrictJSONObject
from wai.json.object.property import StringProperty, BoolProperty


class OrderBy(StrictJSONObject['OrderBy']):
    """
    A filtering stage which specifies the list should be returned
    in order of some field on the model.
    """
    # The field to sort by
    field: str = StringProperty()

    # Whether to sort ascending (the default) or descending
    ascending: bool = BoolProperty(
        optional=True,
        default=True
    )

    # Whether null values are sorted to the beginning or end
    # of the sort order (default is undefined)
    nulls_first: bool = BoolProperty(
        optional=True
    )
