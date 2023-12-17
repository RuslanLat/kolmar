from marshmallow import Schema, fields


class DepartmentSchema(Schema):
    department = fields.Str(required=True)
    email = fields.Str()
    telegram_id = fields.Int()


class DepartmentRequestSchema(DepartmentSchema):
    pass


class DepartmentResponseSchema(Schema):
    department_id = fields.Int(required=True)
    department = fields.Str(required=True)
    email = fields.Str(required=True)
    telegram_id = fields.Int(required=True)


class DepartmentListResponseSchema(Schema):
    departments = fields.Nested(DepartmentResponseSchema, many=True)


class DepartmentBotUpdateSchema(Schema):
    department_id = fields.Int(required=True)
    telegram_id = fields.Int(required=True)


class DepartmentBotResponseSchema(Schema):
    id = fields.Int(required=True)
    department_id = fields.Int(required=True)
    telegram_id = fields.Int(required=True)
    link = fields.Str(required=True) 
    