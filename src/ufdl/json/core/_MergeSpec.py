from wai.json.object import StrictJSONObject
from wai.json.object.property import BoolProperty


class MergeSpec(StrictJSONObject['MergeSpec']):
    """
    Message to merge an object into another.
    """
    # Whether to delete the source object after merging
    delete: bool = BoolProperty()

    # Whether to hard-delete
    hard: bool = BoolProperty(optional=True, default=False)
