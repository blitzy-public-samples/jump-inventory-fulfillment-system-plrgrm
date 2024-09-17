import requests
from typing import Dict
from backend.app.core.config import SENDLE_API_KEY
from backend.app.db.models import Order, ShippingLabel

SENDLE_API_BASE_URL = 'https://api.sendle.com/api/v1'

class SendleService:
    def __init__(self):
        # Initialize any necessary attributes
        self.api_key = SENDLE_API_KEY
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    # HUMAN ASSISTANCE NEEDED
    # This function needs more details about the Sendle API structure and response format
    def generate_shipping_label(self, order: Order) -> ShippingLabel:
        # Prepare shipping details from order
        shipping_details = {
            'pickup_address': {
                'address_line1': order.sender_address_line1,
                'suburb': order.sender_suburb,
                'state_name': order.sender_state,
                'postcode': order.sender_postcode,
                'country': order.sender_country
            },
            'delivery_address': {
                'address_line1': order.recipient_address_line1,
                'suburb': order.recipient_suburb,
                'state_name': order.recipient_state,
                'postcode': order.recipient_postcode,
                'country': order.recipient_country
            },
            'parcel': {
                'weight': order.weight,
                'description': order.description
            }
        }

        # Send POST request to Sendle API
        response = requests.post(
            f'{SENDLE_API_BASE_URL}/labels',
            json=shipping_details,
            headers=self.headers
        )
        response.raise_for_status()

        # Process response and create ShippingLabel object
        label_data = response.json()
        shipping_label = ShippingLabel(
            order_id=order.id,
            tracking_number=label_data['tracking_number'],
            label_url=label_data['label_url'],
            status=label_data['status']
        )

        return shipping_label

    # HUMAN ASSISTANCE NEEDED
    # This function needs more details about the Sendle API response format for tracking info
    def get_tracking_info(self, tracking_number: str) -> Dict:
        # Construct API endpoint for tracking info
        endpoint = f'{SENDLE_API_BASE_URL}/tracking/{tracking_number}'

        # Send GET request to Sendle API
        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()

        # Parse and return the tracking information
        return response.json()