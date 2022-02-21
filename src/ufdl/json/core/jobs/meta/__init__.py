"""
Package defining the JSON structures for specifying the structure of
meta-templates, which coordinate the execution of child templates in
a workflow.
"""
from ._Dependency import Dependency
from ._DependencyGraph import DependencyGraph
from ._Node import Node
from ._ParameterOverrideSpec import ParameterOverrideSpec
