from typing import List

from wai.json.object import StrictJSONObject
from wai.json.object.property import StringProperty, ArrayProperty

from ._InputSpec import InputSpec
from ._ParameterSpec import ParameterSpec


class WorkableTemplateSpec(StrictJSONObject['WorkableTemplateSpec']):
    """
    JSON document specifying parameters for a job template which
    can be worked by worker-nodes.
    """
    # The framework being used by the worker node, in 'name|version' format
    framework: str = StringProperty(min_length=3, max_length=49)

    # The type of job this template performs
    job_type: str = StringProperty(min_length=1, max_length=32)

    # The executor class responsible for executing this template
    executor_class: str = StringProperty(max_length=128)

    # Any packages that the executor class requires to complete the task
    required_packages: str = StringProperty()

    # The body of the job
    body: str = StringProperty()

    # Any inputs to the job required to perform the task
    inputs: List[InputSpec] = ArrayProperty(element_property=InputSpec.as_property())

    # Any parameters to the job required to perform the task
    parameters: List[ParameterSpec] = ArrayProperty(element_property=ParameterSpec.as_property())
