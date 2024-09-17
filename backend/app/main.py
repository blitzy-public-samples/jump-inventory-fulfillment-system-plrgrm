from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from backend.app.api.auth import auth_bp
from backend.app.api.orders import orders_bp
from backend.app.api.inventory import inventory_bp
from backend.app.api.fulfillment import fulfillment_bp
from backend.app.api.reporting import reporting_bp
from backend.app.core.config import load_config
from backend.app.db.database import init_db
from backend.app.services.shopify_service import ShopifyService
from backend.app.services.sendle_service import SendleService

app = Flask(__name__)

def create_app():
    # HUMAN ASSISTANCE NEEDED
    # This function has a confidence level below 0.8. Please review and adjust as necessary.
    
    # Load configuration
    config = load_config()
    app.config.from_object(config)
    
    # Initialize database
    init_db(app)
    
    # Configure CORS
    CORS(app)
    
    # Initialize JWT manager
    jwt = JWTManager(app)
    
    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(inventory_bp)
    app.register_blueprint(fulfillment_bp)
    app.register_blueprint(reporting_bp)
    
    # Initialize Shopify and Sendle services
    app.shopify_service = ShopifyService(config.SHOPIFY_API_KEY, config.SHOPIFY_API_SECRET)
    app.sendle_service = SendleService(config.SENDLE_API_KEY)
    
    # Configure error handlers
    configure_error_handlers(app)
    
    return app

def configure_error_handlers(app):
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({"error": "Not Found"}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)