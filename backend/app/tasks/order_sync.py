from celery import Celery
from backend.app.core.config import SHOPIFY_API_KEY, SHOPIFY_API_SECRET
from backend.app.db.models import Order, OrderItem
from backend.app.services.shopify_service import ShopifyService
from backend.app.db.database import get_db

celery_app = Celery('order_sync', broker=REDIS_URL)

@celery_app.task
def sync_unfulfilled_orders():
    # HUMAN ASSISTANCE NEEDED
    # This function needs review for production readiness and error handling
    
    shopify_service = ShopifyService(SHOPIFY_API_KEY, SHOPIFY_API_SECRET)
    db = next(get_db())
    
    try:
        unfulfilled_orders = shopify_service.get_unfulfilled_orders()
        
        for shopify_order in unfulfilled_orders:
            existing_order = db.query(Order).filter(Order.shopify_id == shopify_order.id).first()
            
            if not existing_order:
                new_order = Order(
                    shopify_id=shopify_order.id,
                    status=shopify_order.financial_status,
                    total_price=shopify_order.total_price,
                    # Add other relevant fields
                )
                db.add(new_order)
                
                for item in shopify_order.line_items:
                    new_item = OrderItem(
                        order=new_order,
                        product_id=item.product_id,
                        variant_id=item.variant_id,
                        quantity=item.quantity,
                        price=item.price,
                        # Add other relevant fields
                    )
                    db.add(new_item)
            else:
                if existing_order.status != shopify_order.financial_status:
                    existing_order.status = shopify_order.financial_status
                    # Update other fields if necessary
        
        db.commit()
    except Exception as e:
        db.rollback()
        # Log the error
        raise
    finally:
        db.close()