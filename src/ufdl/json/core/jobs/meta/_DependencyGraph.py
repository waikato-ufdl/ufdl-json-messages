from typing import Dict, List

from wai.json.object import StrictJSONObject
from wai.json.object.property import MapProperty, ArrayProperty

from ._Dependency import Dependency
from ._Node import Node


class DependencyGraph(StrictJSONObject['DependencyGraph']):
    """
    Graph describing the child templates to a meta-template,
    and the connections between their inputs/outputs.
    """
    # The child templates that participate in this meta-template, keyed by name
    nodes: Dict[str, Node] = MapProperty(
        value_property=Node.as_property()
    )

    # The dependencies between the inputs/outputs of the child templates
    dependencies: List[Dependency] = ArrayProperty(
        element_property=Dependency.as_property()
    )
