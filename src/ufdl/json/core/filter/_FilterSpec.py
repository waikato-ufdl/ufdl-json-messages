from typing import List

from wai.json.object import StrictJSONObject
from wai.json.object.property import ArrayProperty, OneOfProperty

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
                Contains.as_property(),
                Exact.as_property(),
                And.as_property(),
                Or.as_property()
            )
        ),
        optional=True
    )

    # An optional final ordering on the result, in order of precedence
    order_by: List[OrderBy] = ArrayProperty(
        element_property=OrderBy.as_property(),
        optional=True
    )
