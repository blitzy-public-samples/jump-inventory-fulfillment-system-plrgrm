from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.sendle_service import SendleService
from app.db.models import Order, ShippingLabel

fulfillment_bp = Blueprint('fulfillment', __name__)

@fulfillment_bp.route('/<order_id>/label', methods=['POST'])
@jwt_required()
def generate_shipping_label(order_id):
    # HUMAN ASSISTANCE NEEDED
    # This function needs review and potential modifications for production readiness.
    # The confidence level is below 0.8, indicating that some aspects may need improvement.

    # Verify JWT token
    current_user = get_jwt_identity()

    # Retrieve order from database
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    # Generate shipping label using Sendle service
    sendle_service = SendleService()
    try:
        label_data = sendle_service.generate_label(order)
    except Exception as e:
        return jsonify({"error": f"Failed to generate shipping label: {str(e)}"}), 500

    # Save shipping label to database
    shipping_label = ShippingLabel(
        order_id=order.id,
        tracking_number=label_data.get('tracking_number'),
        label_url=label_data.get('label_url')
    )
    db.session.add(shipping_label)
    db.session.commit()

    # Return shipping label details
    return jsonify({
        "order_id": order.id,
        "tracking_number": shipping_label.tracking_number,
        "label_url": shipping_label.label_url
    }), 200