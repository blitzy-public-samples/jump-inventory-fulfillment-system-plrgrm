from celery import Celery
from backend.app.core.config import SHOPIFY_API_KEY, SHOPIFY_API_SECRET
from backend.app.db.models import Product
from backend.app.services.shopify_service import ShopifyService
from backend.app.db.database import get_db

celery_app = Celery('inventory_update', broker=REDIS_URL)

@celery_app.task
def update_inventory_levels():
    # HUMAN ASSISTANCE NEEDED
    # This function has a confidence level of 0.6, which is below the threshold of 0.8.
    # The following implementation may need review and adjustments for production readiness.
    
    shopify_service = ShopifyService(SHOPIFY_API_KEY, SHOPIFY_API_SECRET)
    db = next(get_db())
    
    try:
        products = db.query(Product).all()
        
        for product in products:
            try:
                shopify_service.update_inventory_level(product.shopify_id, product.inventory_quantity)
            except Exception as e:
                # Log the error for this specific product
                print(f"Error updating inventory for product {product.id}: {str(e)}")
        
        print("Inventory update completed successfully")
    except Exception as e:
        # Log any general errors
        print(f"Error during inventory update: {str(e)}")
    finally:
        db.close()