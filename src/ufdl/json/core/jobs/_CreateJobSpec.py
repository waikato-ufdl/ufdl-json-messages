from typing import Union

from wai.json.object import StrictJSONObject
from wai.json.object.property import NumberProperty, OneOfProperty, StringProperty

from ._DockerImageSpec import DockerImageSpec
from ._Values import Values


class CreateJobSpec(StrictJSONObject['CreateJobSpec']):
    """
    Specifies the JSON data structure for specifying the arguments
    to execute a job-template with.
    """
    # The Docker image to run the job (by pk or name/version)
    docker_image: Union[int, DockerImageSpec] = OneOfProperty(
        sub_properties=(
            NumberProperty(minimum=1, integer_only=True),
            DockerImageSpec.as_property()
        )
    )

    # The values of the inputs
    input_values: Values = Values.as_property()

    # The values of the parameters
    parameter_values: Values = Values.as_property(optional=True)

    # A description of the job
    description: str = StringProperty(optional=True, default="")
