import unittest
from unittest.mock import patch, MagicMock
from services.shopify_service import ShopifyService
from services.sendle_service import SendleService
from services.inventory_service import InventoryService
from services.order_service import OrderService
from services.reporting_service import ReportingService

class TestShopifyService(unittest.TestCase):
    def setUp(self):
        self.shopify_service = ShopifyService()

    @patch('services.shopify_service.shopify')
    def test_fetch_orders(self, mock_shopify):
        mock_shopify.Order.find.return_value = [MagicMock(id=1), MagicMock(id=2)]
        orders = self.shopify_service.fetch_orders()
        self.assertEqual(len(orders), 2)
        mock_shopify.Order.find.assert_called_once()

    @patch('services.shopify_service.shopify')
    def test_update_order_status(self, mock_shopify):
        mock_order = MagicMock()
        mock_shopify.Order.find.return_value = mock_order
        self.shopify_service.update_order_status(1, 'fulfilled')
        mock_order.fulfillment_status.assert_called_with('fulfilled')
        mock_order.save.assert_called_once()

class TestSendleService(unittest.TestCase):
    def setUp(self):
        self.sendle_service = SendleService()

    @patch('services.sendle_service.requests')
    def test_create_shipment(self, mock_requests):
        mock_response = MagicMock()
        mock_response.json.return_value = {'tracking_number': '123456'}
        mock_requests.post.return_value = mock_response

        result = self.sendle_service.create_shipment({
            'from_address': '123 Sender St, City, Country',
            'to_address': '456 Receiver St, City, Country',
            'parcel': {'weight': 1.5, 'dimensions': {'length': 10, 'width': 10, 'height': 10}}
        })

        self.assertEqual(result['tracking_number'], '123456')
        mock_requests.post.assert_called_once()

class TestInventoryService(unittest.TestCase):
    def setUp(self):
        self.inventory_service = InventoryService()

    @patch('services.inventory_service.db')
    def test_update_stock_level(self, mock_db):
        mock_product = MagicMock()
        mock_db.session.query.return_value.filter_by.return_value.first.return_value = mock_product

        self.inventory_service.update_stock_level('SKU123', 10)

        self.assertEqual(mock_product.stock_level, 10)
        mock_db.session.commit.assert_called_once()

    @patch('services.inventory_service.db')
    def test_get_low_stock_items(self, mock_db):
        mock_db.session.query.return_value.filter.return_value.all.return_value = [
            MagicMock(sku='SKU1', stock_level=5),
            MagicMock(sku='SKU2', stock_level=3)
        ]

        low_stock_items = self.inventory_service.get_low_stock_items(threshold=10)

        self.assertEqual(len(low_stock_items), 2)
        self.assertEqual(low_stock_items[0]['sku'], 'SKU1')
        self.assertEqual(low_stock_items[1]['sku'], 'SKU2')

class TestOrderService(unittest.TestCase):
    def setUp(self):
        self.order_service = OrderService()

    @patch('services.order_service.db')
    @patch('services.order_service.ShopifyService')
    @patch('services.order_service.SendleService')
    def test_process_order(self, mock_sendle, mock_shopify, mock_db):
        mock_order = MagicMock(id=1, line_items=[MagicMock(sku='SKU123', quantity=2)])
        mock_shopify.return_value.fetch_order.return_value = mock_order
        mock_sendle.return_value.create_shipment.return_value = {'tracking_number': '123456'}

        result = self.order_service.process_order(1)

        self.assertEqual(result['order_id'], 1)
        self.assertEqual(result['tracking_number'], '123456')
        mock_shopify.return_value.update_order_status.assert_called_with(1, 'fulfilled')
        mock_db.session.commit.assert_called_once()

class TestReportingService(unittest.TestCase):
    def setUp(self):
        self.reporting_service = ReportingService()

    @patch('services.reporting_service.db')
    def test_generate_sales_report(self, mock_db):
        mock_db.session.query.return_value.filter.return_value.all.return_value = [
            MagicMock(id=1, total_amount=100),
            MagicMock(id=2, total_amount=200)
        ]

        report = self.reporting_service.generate_sales_report('2023-01-01', '2023-01-31')

        self.assertEqual(report['total_sales'], 300)
        self.assertEqual(report['num_orders'], 2)

    @patch('services.reporting_service.db')
    def test_generate_inventory_report(self, mock_db):
        mock_db.session.query.return_value.all.return_value = [
            MagicMock(sku='SKU1', stock_level=10),
            MagicMock(sku='SKU2', stock_level=5)
        ]

        report = self.reporting_service.generate_inventory_report()

        self.assertEqual(len(report['items']), 2)
        self.assertEqual(report['items'][0]['sku'], 'SKU1')
        self.assertEqual(report['items'][1]['sku'], 'SKU2')

if __name__ == '__main__':
    unittest.main()