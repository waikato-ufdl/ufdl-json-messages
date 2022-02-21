from typing import Dict

from wai.json.object import StrictJSONObject
from wai.json.object.property import StringProperty, NumberProperty, MapProperty

from ._ParameterOverrideSpec import ParameterOverrideSpec


class Node(StrictJSONObject['Node']):
    """
    A node in a dependency graph, indicating which template to use
    to create sub-jobs of the meta-template.
    """
    # The name of the job template to use for this node
    name: str = StringProperty(
        min_length=1,
        max_length=200
    )

    # The version of the template to use (uses the latest if omitted)
    version: int = NumberProperty(
        minimum=1,
        integer_only=True,
        optional=True
    )

    # The values to use as default for this node's parameters, overriding
    # the defaults defined on the child template
    parameter_default_overrides: Dict[str, ParameterOverrideSpec] = MapProperty(
        value_property=ParameterOverrideSpec.as_property(),
        optional=True
    )
