from marshmallow import Schema, fields


class SubdivisionSchema(Schema):
    subdivision = fields.Str(required=True)
    email = fields.Str()
    telegram_id = fields.Int()


class SubdivisionRequestSchema(SubdivisionSchema):
    pass


class SubdivisionResponseSchema(Schema):
    subdivision_id = fields.Int(required=True)
    subdivision = fields.Str(required=True)
    email = fields.Str(required=True)
    telegram_id = fields.Int(required=True)


class SubdivisionListResponseSchema(Schema):
    subdivisions = fields.Nested(SubdivisionResponseSchema, many=True)


class SubdivisionBotUpdateSchema(Schema):
    subdivision_id = fields.Int(required=True)
    telegram_id = fields.Int(required=True)


class SubdivisionBotResponseSchema(Schema):
    id = fields.Int(required=True)
    subdivision_id = fields.Int(required=True)
    telegram_id = fields.Int(required=True)
    link = fields.Str(required=True) 
