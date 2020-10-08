from wai.json.object import JSONObject
from wai.json.object.property import StringProperty


class PretrainedModelMigrationSpec(JSONObject['PretrainedModelMigrationSpec']):
    """
    Represents the JSON structure used to specify a pre-trained model in
    the migration of the database.
    """
    name = StringProperty(min_length=1, max_length=200)
    description = StringProperty()
    url = StringProperty(min_length=1, max_length=200)
    licence = StringProperty(min_length=1, max_length=100)
    framework = StringProperty(min_length=3, max_length=49)
    domain = StringProperty(min_length=1, max_length=2)
    source = StringProperty()
    metadata = JSONObject.as_property()
