from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, email: str, password_hash: str, role: str):
        self.email = email
        self.password_hash = password_hash
        self.role = role
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    sku = Column(String, unique=True, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, name: str, description: str, sku: str, quantity: int, price: float):
        self.name = name
        self.description = description
        self.sku = sku
        self.quantity = quantity
        self.price = price
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    shopify_order_id = Column(String, unique=True, nullable=False)
    status = Column(String, nullable=False)
    order_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    order_items = relationship("OrderItem", back_populates="order")
    shipping_label = relationship("ShippingLabel", back_populates="order", uselist=False)

    def __init__(self, shopify_order_id: str, status: str, order_date: datetime):
        self.shopify_order_id = shopify_order_id
        self.status = status
        self.order_date = order_date
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    order = relationship("Order", back_populates="order_items")
    product = relationship("Product")

    def __init__(self, order_id: int, product_id: int, quantity: int, price: float):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

class ShippingLabel(Base):
    __tablename__ = 'shipping_labels'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    tracking_number = Column(String, nullable=False)
    carrier = Column(String, nullable=False)
    label_data = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    order = relationship("Order", back_populates="shipping_label")

    def __init__(self, order_id: int, tracking_number: str, carrier: str, label_data: str):
        self.order_id = order_id
        self.tracking_number = tracking_number
        self.carrier = carrier
        self.label_data = label_data
        self.created_at = datetime.utcnow()

class InventoryAdjustment(Base):
    __tablename__ = 'inventory_adjustments'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity_change = Column(Integer, nullable=False)
    reason = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    product = relationship("Product")

    def __init__(self, product_id: int, quantity_change: int, reason: str):
        self.product_id = product_id
        self.quantity_change = quantity_change
        self.reason = reason
        self.created_at = datetime.utcnow()