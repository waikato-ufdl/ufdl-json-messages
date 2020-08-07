from wai.json.object import StrictJSONObject
from wai.json.object.property import StringProperty


class DockerImageSpec(StrictJSONObject['DockerImageSpec']):
    """
    Specifies the JSON data structure for specifying the a
    particular docker image.
    """
    # The name of the Docker image
    name: str = StringProperty(min_length=1, max_length=64)

    # The version of the Docker image
    version: str = StringProperty(min_length=1, max_length=32)
