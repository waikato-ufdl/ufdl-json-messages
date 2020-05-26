from typing import List

from wai.json.object import StrictJSONObject
from wai.json.object.property import StringProperty, EnumProperty, ArrayProperty


class LicenceSubdescriptorModSpec(StrictJSONObject['LicenceSubdescriptorModSpec']):
    """
    Message to modify the sub-descriptors of a licence.
    """
    # The type of sub-descriptor to modify
    type: str = EnumProperty(values=("permission", "condition", "limitation"))

    # The type of modification to make
    method: str = EnumProperty(values=("add", "remove"))

    # The name of the sub-descriptor
    name: List[str] = ArrayProperty(element_property=StringProperty(min_length=1), min_elements=1, unique_elements=True)
