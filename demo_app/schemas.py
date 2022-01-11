from marshmallow import Schema, fields, pre_load, validate


class UserSchema(Schema):
    name = fields.Str(validate=validate.Length(min=1, max=50))
    active = fields.Bool()
    country = fields.Str(validate=validate.Length(min=1, max=20))

    @pre_load
    def process_input(self, data, **kwargs):
        data['name'] = data.get('name', '').strip()
        data['country'] = data.get('country', '').strip()
        return data
