from wai.json.object import JSONObject
from wai.json.object.property import StringProperty, ArrayProperty


class JobTemplateMigrationSpec(JSONObject['JobTemplateMigrationSpec']):
    """
    Specification of the JSON format used to describe pre-defined
    job templates to the Django migration system.
    """
    name = StringProperty(min_length=1, max_length=64)
    scope = StringProperty(min_length=1, max_length=16)
    framework = StringProperty(min_length=3, max_length=49)
    domain = StringProperty(min_length=2, max_length=2)
    job_type = StringProperty(min_length=1, max_length=32)
    executor_class = StringProperty(min_length=1, max_length=128)
    required_packages = StringProperty()
    body = StringProperty(min_length=1)
    licence = StringProperty(min_length=1, max_length=100)
    inputs = ArrayProperty(element_property=StringProperty())
    parameters = ArrayProperty(element_property=StringProperty())
