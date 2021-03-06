from typing import List

from wai.json.object import StrictJSONObject
from wai.json.object.property import ArrayProperty, OneOfProperty, BoolProperty

from .field import *
from .logical import *
from ._FilterExpression import FilterExpression
from ._OrderBy import OrderBy


class FilterSpec(StrictJSONObject['FilterSpec']):
    """
    The top-level document describing how to filter a list request.
    """
    # The sequential stages of filters of the list request
    expressions: List[FilterExpression] = ArrayProperty(
        element_property=OneOfProperty(
            sub_properties=(
                And.as_property(),
                Or.as_property(),
                *(field_filter_expression.as_property()
                  for field_filter_expression in ALL_FIELD_FILTER_EXPRESSIONS)
            )
        ),
        optional=True
    )

    # An optional final ordering on the result, in order of precedence
    order_by: List[OrderBy] = ArrayProperty(
        element_property=OrderBy.as_property(),
        optional=True
    )

    # An optional flag to include soft-deleted models as well
    include_inactive: bool = BoolProperty(
        optional=True,
        default=False
    )
