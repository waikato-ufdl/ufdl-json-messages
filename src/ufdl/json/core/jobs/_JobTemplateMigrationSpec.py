from typing import List

from wai.json.object import JSONObject
from wai.json.object.property import StringProperty, ArrayProperty


class InputMigrationSpec(JSONObject['InputMigrationSpec']):
    """
    JSON format for individual inputs in the migration of job-templates.
    """
    name: str = StringProperty(min_length=1, max_length=32)
    type: str = StringProperty(min_length=1, max_length=32)
    options: str = StringProperty(optional=True, default="")
    help: str = StringProperty(optional=True, default="")


class ParameterMigrationSpec(JSONObject['ParameterMigrationSpec']):
    """
    JSON format for individual parameters in the migration of job-templates.
    """
    name: str = StringProperty(min_length=1, max_length=32)
    type: str = StringProperty(min_length=1, max_length=32)
    default: str = StringProperty(optional=True, default="")
    help: str = StringProperty(optional=True, default="")


class JobTemplateMigrationSpec(JSONObject['JobTemplateMigrationSpec']):
    """
    Specification of the JSON format used to describe pre-defined
    job templates to the Django migration system.
    """
    name: str = StringProperty(min_length=1, max_length=64)
    scope: str = StringProperty(min_length=1, max_length=16)
    framework: str = StringProperty(min_length=3, max_length=49)
    domain: str = StringProperty(min_length=2, max_length=2)
    job_type: str = StringProperty(min_length=1, max_length=32)
    executor_class: str = StringProperty(min_length=1, max_length=128)
    required_packages: str = StringProperty()
    body: str = StringProperty(min_length=1)
    licence: str = StringProperty(min_length=1, max_length=100)
    inputs: List[InputMigrationSpec] = ArrayProperty(element_property=InputMigrationSpec.as_property())
    parameters: List[ParameterMigrationSpec] = ArrayProperty(element_property=ParameterMigrationSpec.as_property())
