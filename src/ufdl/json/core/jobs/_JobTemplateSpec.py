from typing import Union

from wai.json.object import StrictJSONObject
from wai.json.object.property import StringProperty, NumberProperty, OneOfProperty

from .meta import DependencyGraph
from ._WorkableTemplateSpec import WorkableTemplateSpec


class JobTemplateSpec(StrictJSONObject['JobTemplateSpec']):
    """
    JSON document which specifies a job template.
    """
    # The name to give the template
    name: str = StringProperty(min_length=1, max_length=200)

    # The version to give the template (omit for latest version)
    version: int = NumberProperty(minimum=1, integer_only=True, optional=True)

    # A description of the task the template performs
    description: str = StringProperty(optional=True, default="")

    # The scope of the template
    scope: str = StringProperty(min_length=1, max_length=16)

    # The licence the template is issued under
    licence: str = StringProperty(min_length=1, max_length=100)

    # The domain of the template, if any
    domain: str = StringProperty(min_length=2, max_length=2, optional=True)

    # The specific information which determines what type of template is defined
    specific: Union[WorkableTemplateSpec, DependencyGraph] = OneOfProperty(
        sub_properties=(
            # Defines a base workable job template
            WorkableTemplateSpec.as_property(),

            # Defines a workflow meta-job template
            DependencyGraph.as_property()
        )
    )
