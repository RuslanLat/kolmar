from marshmallow import Schema, fields


class PredictSchema(Schema):
    date = fields.DateTime()
    user_id = fields.Int(required=True)
    dismiss = fields.Boolean(required=True)
    probability = fields.Float(required=True)


class PredictRequestSchema(PredictSchema):
    pass


class PredictListRequestSchema(Schema):
    predicts = fields.Nested(PredictSchema, many=True)


class PredictDeleteRequestSchema(Schema):
    row_id = fields.Int(required=True)


class PredictResponseSchema(Schema):
    row_id = fields.Int(required=True)
    date = fields.DateTime(required=True)
    user_id = fields.Int(required=True)
    dismiss = fields.Boolean(required=True)
    probability = fields.Float(required=True)


class PredictListResponseSchema(Schema):
    predicts = fields.Nested(PredictResponseSchema, many=True)
