"""
Package for filter expressions which operate on a particular field
of a model.
"""
from ._Compare import Compare
from ._Contains import Contains
from ._Exact import Exact
from ._FieldFilterExpression import FieldFilterExpression
from ._IsNull import IsNull

# The set of all concrete field filter-expressions
ALL_FIELD_FILTER_EXPRESSIONS = frozenset((Compare, Contains, Exact, IsNull))
