from marshmallow import Schema, fields
from typing import List

class OrderItemSchema(Schema):
    product_id = fields.Str()
    sku = fields.Str()
    name = fields.Str()
    quantity = fields.Int()
    price = fields.Float()

class OrderSchema(Schema):
    id = fields.Str()
    shopify_order_id = fields.Str()
    status = fields.Str()
    order_date = fields.DateTime()
    items = fields.List(fields.Nested(OrderItemSchema))
    customer_name = fields.Str()
    shipping_address = fields.Str()
    total_amount = fields.Float()