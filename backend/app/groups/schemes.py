from marshmallow import Schema, fields


class GroupSchema(Schema):
    group = fields.Str(required=True)


class GroupRequestSchema(GroupSchema):
    pass


class GroupResponseSchema(Schema):
    group_id = fields.Int(required=True)
    group = fields.Str(required=True)


class GroupListResponseSchema(Schema):
    groups = fields.Nested(GroupResponseSchema, many=True)
