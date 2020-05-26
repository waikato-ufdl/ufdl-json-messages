from typing import List, Union

from wai.json.object import StrictJSONObject
from wai.json.object.property import StringProperty, EnumProperty, ArrayProperty, OneOfProperty, NumberProperty


class LicenceSubdescriptorModSpec(StrictJSONObject['LicenceSubdescriptorModSpec']):
    """
    Message to modify the sub-descriptors of a licence.
    """
    # The type of sub-descriptor to modify
    type: str = EnumProperty(values=("permissions", "conditions", "limitations"))

    # The type of modification to make
    method: str = EnumProperty(values=("add", "remove"))

    # The name of the sub-descriptor
    names: List[Union[str, int]] = ArrayProperty(
        element_property=OneOfProperty(
            sub_properties=(
                StringProperty(min_length=1, max_length=100),
                NumberProperty(minimum=1, integer_only=True)
            )),
        min_elements=1,
        unique_elements=True
    )
