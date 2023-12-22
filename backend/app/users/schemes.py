from marshmallow import Schema, fields


class UserLoginBaseSchema(Schema):
    login = fields.Str(required=True)


class UserLoginRequestSchema(UserLoginBaseSchema):
    password = fields.Str(required=True)


class UserLoginResponseSchema(UserLoginBaseSchema):
    id = fields.Int(required=True)


class UserLoginUpdateRequestSchema(UserLoginRequestSchema):
    pass


class UserLoginListResponseSchema(Schema):
    users = fields.Nested(UserLoginResponseSchema, many=True)


class UserBaseSchema(Schema):
    name = fields.Str(required=True)
    lastname = fields.Str(required=True)
    male = fields.Boolean(required=True)
    age = fields.Int(required=True)
    experience = fields.Int(required=True)
    is_view = fields.Boolean()
    department_id = fields.Int(required=True)
    subdivision_id = fields.Int(required=True)
    position_id = fields.Int(required=True)
    role_id = fields.Int(required=True)
    email = fields.Str()
    telegram_id = fields.Int()
    fired = fields.Boolean()


class UserRequestSchema(UserBaseSchema):
    pass


class UserInsertRequestSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    lastname = fields.Str(required=True)
    male = fields.Boolean(required=True)
    age = fields.Int(required=True)
    experience = fields.Int(required=True)
    # email = fields.Str()
    # telegram_id = fields.Int()


class UserUpdateRequestSchema(UserBaseSchema):
    id = fields.Int(required=True)
    is_view = fields.Boolean(required=True)


class UserResponseSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    lastname = fields.Str(required=True)
    male = fields.Boolean(required=True)
    age = fields.Int(required=True)
    experience = fields.Int(required=True)
    is_view = fields.Boolean(required=True)
    department_id = fields.Int(required=True)
    subdivision_id = fields.Int(required=True)
    position_id = fields.Int(required=True)
    role_id = fields.Int(required=True)
    email = fields.Str(required=True)
    telegram_id = fields.Int(required=True)
    fired = fields.Boolean(required=True)


class UserListResponseSchema(Schema):
    users = fields.Nested(UserResponseSchema, many=True)


class UserFullResponseSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    lastname = fields.Str(required=True)
    male = fields.Boolean(required=True)
    age = fields.Int(required=True)
    experience = fields.Int(required=True)
    is_view = fields.Boolean(required=True)
    department = fields.Str(required=True)
    subdivision = fields.Str(required=True)
    position = fields.Str(required=True)
    role = fields.Str(required=True)
    email = fields.Str(required=True)
    telegram_id = fields.Int(required=True)
    fired = fields.Boolean(required=True)


class UserFullListResponseSchema(Schema):
    users = fields.Nested(UserFullResponseSchema, many=True)


class UserBotFull(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    lastname = fields.Str(required=True)
    # is_view = fields.Boolean()
    # group_id = fields.Int()


class UserBotFullListResponseSchema(Schema):
    users = fields.Nested(UserBotFull, many=True)
