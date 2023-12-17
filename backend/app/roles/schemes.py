from marshmallow import Schema, fields


class RoleSchema(Schema):
    role = fields.Str(required=True)


class RoleRequestSchema(RoleSchema):
    pass


class RoleResponseSchema(Schema):
    role_id = fields.Int(required=True)
    role = fields.Str(required=True)


class RoleUpdateRequestSchema(RoleResponseSchema):
    pass


class RoleListResponseSchema(Schema):
    roles = fields.Nested(RoleResponseSchema, many=True)
