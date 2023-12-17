from marshmallow import Schema, fields


class EmailSchema(Schema):
    user_id = fields.Int(required=True)
    date = fields.DateTime(required=True)
    use_email_total = fields.Int(required=True)
    active_use_email = fields.Int(required=True)
    use_email_last = fields.Int(required=True)
    out_work_internal_email_total = fields.Int(required=True)
    out_work_internal_email_last = fields.Int(required=True)
    out_work_external_email_total = fields.Int(required=True)
    out_work_external_email_last = fields.Int(required=True)
    cnt_days_pause_total = fields.Int(required=True)
    cnt_days_pause_last = fields.Int(required=True)
    cnt_4hours_later_total = fields.Int(required=True)
    cnt_4hours_later_last = fields.Int(required=True)
    total_letters_total = fields.Int(required=True)
    total_letters_last = fields.Int(required=True)
    received_total = fields.Int(required=True)
    received_last = fields.Int(required=True)
    answer_total = fields.Int(required=True)
    answer_last = fields.Int(required=True)
    out_work_email_total = fields.Int(required=True)
    out_work_email_last = fields.Int(required=True)
    external_email_total = fields.Int(required=True)
    external_email_last = fields.Int(required=True)
    internal_email_total = fields.Int(required=True)
    internal_email_last = fields.Int(required=True)
    cnt_addressees = fields.Int(required=True)
    cnt_address_copy_total = fields.Int(required=True)
    cnt_address_copy_last = fields.Int(required=True)
    cnt_address_hidden_copy_total = fields.Int(required=True)
    cnt_address_hidden_copy_last = fields.Int(required=True)
    div_bytes_emails = fields.Int(required=True)
    cnt_question_incoming = fields.Int(required=True)
    cnt_text_mean_total = fields.Float(required=True)
    cnt_text_mean_last = fields.Float(required=True)


class EmailRequestSchema(EmailSchema):
    pass


class EmailListRequestSchema(Schema):
    emails = fields.Nested(EmailSchema, many=True)


class EmailResponseSchema(Schema):
    row_id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    date = fields.DateTime(required=True)
    use_email_total = fields.Int(required=True)
    active_use_email = fields.Int(required=True)
    use_email_last = fields.Int(required=True)
    out_work_internal_email_total = fields.Int(required=True)
    out_work_internal_email_last = fields.Int(required=True)
    out_work_external_email_total = fields.Int(required=True)
    out_work_external_email_last = fields.Int(required=True)
    cnt_days_pause_total = fields.Int(required=True)
    cnt_days_pause_last = fields.Int(required=True)
    cnt_4hours_later_total = fields.Int(required=True)
    cnt_4hours_later_last = fields.Int(required=True)
    total_letters_total = fields.Int(required=True)
    total_letters_last = fields.Int(required=True)
    received_total = fields.Int(required=True)
    received_last = fields.Int(required=True)
    answer_total = fields.Int(required=True)
    answer_last = fields.Int(required=True)
    out_work_email_total = fields.Int(required=True)
    out_work_email_last = fields.Int(required=True)
    external_email_total = fields.Int(required=True)
    external_email_last = fields.Int(required=True)
    internal_email_total = fields.Int(required=True)
    internal_email_last = fields.Int(required=True)
    cnt_addressees = fields.Int(required=True)
    cnt_address_copy_total = fields.Int(required=True)
    cnt_address_copy_last = fields.Int(required=True)
    cnt_address_hidden_copy_total = fields.Int(required=True)
    cnt_address_hidden_copy_last = fields.Int(required=True)
    div_bytes_emails = fields.Int(required=True)
    cnt_question_incoming = fields.Int(required=True)
    cnt_text_mean_total = fields.Float(required=True)
    cnt_text_mean_last = fields.Float(required=True)


class EmailDeleteRequestSchema(Schema):
    row_id = fields.Int(required=True)


class EmailUserRequestSchema(Schema):
    user_id = fields.Int(required=True)
    week = fields.Int()


class EmailListResponseSchema(Schema):
    emails = fields.Nested(EmailResponseSchema, many=True)
