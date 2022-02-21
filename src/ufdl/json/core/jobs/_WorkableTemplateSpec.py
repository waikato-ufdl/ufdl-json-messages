from typing import Dict

from wai.json.object import StrictJSONObject
from wai.json.object.property import StringProperty, MapProperty

from ._ParameterSpec import ParameterSpec


class WorkableTemplateSpec(StrictJSONObject['WorkableTemplateSpec']):
    """
    JSON document specifying parameters for a job template which
    can be worked by worker-nodes.
    """
    # The type of job this template performs
    job_type: str = StringProperty(min_length=1, max_length=256)

    # The executor class responsible for executing this template
    executor_class: str = StringProperty(max_length=128)

    # Any packages that the executor class requires to complete the task
    required_packages: str = StringProperty()

    # Any parameters to the job required to perform the task
    parameters: Dict[str, ParameterSpec] = MapProperty(value_property=ParameterSpec.as_property())
