from marshmallow import Schema, fields

class ProductSchema(Schema):
    id = fields.Str()
    name = fields.Str()
    description = fields.Str()
    sku = fields.Str()
    quantity = fields.Int()
    price = fields.Float()