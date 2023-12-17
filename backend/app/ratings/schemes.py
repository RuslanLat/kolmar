from marshmallow import Schema, fields


class RatingSchema(Schema):
    user_id = fields.Int(required=True)
    rating = fields.Int(required=True)


class RatingRequestSchema(RatingSchema):
    pass


class RatingResponseSchema(Schema):
    row_id = fields.Int(required=True)
    date = fields.DateTime(required=True)
    user_id = fields.Int(required=True)
    rating = fields.Int(required=True)


class RatingDeleteRequestSchema(Schema):
    row_id = fields.Int(required=True)


class RatingListResponseSchema(Schema):
    ratings = fields.Nested(RatingResponseSchema, many=True)
