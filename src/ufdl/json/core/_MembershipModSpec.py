from wai.json.object import StrictJSONObject
from wai.json.object.property import StringProperty, EnumProperty


class MembershipModSpec(StrictJSONObject['MembershipModSpec']):
    """
    Message to modify the memberships of a team.
    """
    # The username of the membership to modify
    username: str = StringProperty(min_length=1)

    # The type of modification to make
    method: str = EnumProperty(values=("add", "remove", "update"))

    # The permissions to give the member (only required for 'add' and 'update',
    # defaults to read-only permission if not specified).
    permissions: str = EnumProperty(values=("R", "X", "W", "A"), optional=True, default="R")
