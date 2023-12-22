from marshmallow import Schema, fields


class StimulSchema(Schema):
    user_id = fields.Int()
    date = fields.DateTime()
    q1 = fields.String(required=True)
    q2 = fields.String(required=True)
    q3 = fields.String(required=True)
    q4 = fields.String(required=True)
    q5 = fields.String(required=True)
    q6 = fields.String(required=True)
    q7 = fields.String(required=True)
    q8 = fields.String(required=True)
    q9 = fields.String(required=True)
    q10 = fields.String(required=True)
    q11 = fields.String(required=True)


class StimulRequestSchema(StimulSchema):
    name = fields.String(required=True)
    lastname = fields.String(required=True)


class StimulResponseSchema(Schema):
    row_id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    date = fields.DateTime(required=True)
    q1 = fields.String(required=True)
    q2 = fields.String(required=True)
    q3 = fields.String(required=True)
    q4 = fields.String(required=True)
    q5 = fields.String(required=True)
    q6 = fields.String(required=True)
    q7 = fields.String(required=True)
    q8 = fields.String(required=True)
    q9 = fields.String(required=True)
    q10 = fields.String(required=True)
    q11 = fields.String(required=True)


class StimulListResponseSchema(Schema):
    stimuls = fields.Nested(StimulResponseSchema, many=True)
