from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.db.models import Product
from app.schema.product import ProductSchema

inventory_bp = Blueprint('inventory', __name__)

@inventory_bp.route('', methods=['GET'])
@jwt_required()
def get_inventory():
    # Verify JWT token
    current_user = get_jwt_identity()
    
    # Query inventory items from database
    products = Product.query.all()
    
    # Serialize and return inventory items
    product_schema = ProductSchema(many=True)
    return jsonify(product_schema.dump(products)), 200

@inventory_bp.route('/update', methods=['POST'])
@jwt_required()
def update_inventory():
    # HUMAN ASSISTANCE NEEDED
    # This function needs additional error handling and input validation
    # Verify JWT token
    current_user = get_jwt_identity()
    
    # Extract inventory updates from request
    updates = request.json.get('updates', [])
    
    # Validate update data
    if not updates or not isinstance(updates, list):
        return jsonify({"error": "Invalid update data"}), 400
    
    # Update inventory in database
    updated_products = []
    for update in updates:
        product_id = update.get('id')
        new_quantity = update.get('quantity')
        
        if not product_id or not isinstance(new_quantity, int):
            return jsonify({"error": f"Invalid update data for product {product_id}"}), 400
        
        product = Product.query.get(product_id)
        if not product:
            return jsonify({"error": f"Product with id {product_id} not found"}), 404
        
        product.quantity = new_quantity
        updated_products.append(product)
    
    # Commit changes to database
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to update inventory"}), 500
    
    # Return update status
    return jsonify({"message": "Inventory updated successfully", "updated_count": len(updated_products)}), 200