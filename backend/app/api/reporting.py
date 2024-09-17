from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.db.models import Order, Product
from app.services.reporting_service import generate_inventory_report, generate_fulfillment_report

reporting_bp = Blueprint('reporting', __name__)

@reporting_bp.route('/inventory', methods=['GET'])
@jwt_required()
def get_inventory_report():
    # HUMAN ASSISTANCE NEEDED
    # This function needs review for production readiness
    try:
        # Verify JWT token
        current_user = get_jwt_identity()
        
        # Generate inventory report
        report_data = generate_inventory_report()
        
        # Return report data
        return jsonify({"status": "success", "data": report_data}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@reporting_bp.route('/fulfillment', methods=['GET'])
@jwt_required()
def get_fulfillment_report():
    # HUMAN ASSISTANCE NEEDED
    # This function needs review for production readiness
    try:
        # Verify JWT token
        current_user = get_jwt_identity()
        
        # Generate fulfillment report
        report_data = generate_fulfillment_report()
        
        # Return report data
        return jsonify({"status": "success", "data": report_data}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500