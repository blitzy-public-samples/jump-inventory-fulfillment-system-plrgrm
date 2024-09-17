from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.db.models import Order, OrderItem
from app.services.shopify_service import ShopifyService
from app.schema.order import OrderSchema

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('', methods=['GET'])
@jwt_required()
def get_orders():
    # HUMAN ASSISTANCE NEEDED
    # This function needs review for production readiness
    try:
        # Verify JWT token
        current_user = get_jwt_identity()
        
        # Extract query parameters
        status = request.args.get('status')
        
        # Query orders from database
        if status:
            orders = Order.query.filter_by(status=status).all()
        else:
            orders = Order.query.all()
        
        # Serialize and return orders
        order_schema = OrderSchema(many=True)
        return jsonify(orders=order_schema.dump(orders)), 200
    except Exception as e:
        return jsonify(error=str(e)), 500

@orders_bp.route('/<order_id>', methods=['GET'])
@jwt_required()
def get_order(order_id):
    try:
        # Verify JWT token
        current_user = get_jwt_identity()
        
        # Query order from database
        order = Order.query.get(order_id)
        if not order:
            return jsonify(error="Order not found"), 404
        
        # Serialize and return order details
        order_schema = OrderSchema()
        return jsonify(order=order_schema.dump(order)), 200
    except Exception as e:
        return jsonify(error=str(e)), 500

@orders_bp.route('/<order_id>/fulfill', methods=['POST'])
@jwt_required()
def fulfill_order(order_id):
    # HUMAN ASSISTANCE NEEDED
    # This function needs review for production readiness and error handling
    try:
        # Verify JWT token
        current_user = get_jwt_identity()
        
        # Retrieve order from database
        order = Order.query.get(order_id)
        if not order:
            return jsonify(error="Order not found"), 404
        
        # Validate order can be fulfilled
        if order.status != 'pending':
            return jsonify(error="Order cannot be fulfilled"), 400
        
        # Process fulfillment with Shopify
        shopify_service = ShopifyService()
        fulfillment_result = shopify_service.fulfill_order(order)
        
        # Update order status in database
        if fulfillment_result['success']:
            order.status = 'fulfilled'
            order.save()
        
        # Return fulfillment status
        return jsonify(fulfillment_status=fulfillment_result), 200
    except Exception as e:
        return jsonify(error=str(e)), 500