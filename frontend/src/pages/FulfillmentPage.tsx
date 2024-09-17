import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import BarcodeScanner from 'frontend/src/components/FulfillmentProcess/BarcodeScanner';
import ShippingLabelGenerator from 'frontend/src/components/FulfillmentProcess/ShippingLabelGenerator';
import { fulfillOrderThunk } from 'frontend/src/store/orderSlice';

// HUMAN ASSISTANCE NEEDED
// This component needs further refinement and error handling for production readiness.
// The following areas need attention:
// - Proper type definitions for state and Redux store
// - Error handling for API calls and user interactions
// - Accessibility improvements
// - Performance optimizations
// - Unit and integration tests

const FulfillmentPage: React.FC = () => {
  const dispatch = useDispatch();
  const selectedOrder = useSelector((state: any) => state.orders.selectedOrder);
  const [scannedItems, setScannedItems] = useState<string[]>([]);
  const [allItemsVerified, setAllItemsVerified] = useState(false);

  const handleBarcodeScanned = (barcode: string) => {
    if (selectedOrder.items.some((item: any) => item.barcode === barcode)) {
      setScannedItems([...scannedItems, barcode]);
      if (scannedItems.length + 1 === selectedOrder.items.length) {
        setAllItemsVerified(true);
      }
    } else {
      // Handle invalid barcode
      console.error('Invalid barcode scanned');
    }
  };

  const handleFulfillOrder = async () => {
    try {
      await dispatch(fulfillOrderThunk(selectedOrder.id));
      // Handle successful fulfillment (e.g., show success message, redirect)
    } catch (error) {
      // Handle fulfillment error
      console.error('Error fulfilling order:', error);
    }
  };

  return (
    <div className="fulfillment-page">
      <h1>Order Fulfillment</h1>
      {selectedOrder && (
        <div className="order-details">
          <h2>Order #{selectedOrder.id}</h2>
          <p>Customer: {selectedOrder.customerName}</p>
          <ul>
            {selectedOrder.items.map((item: any) => (
              <li key={item.id}>
                {item.name} - {item.quantity}x
                {scannedItems.includes(item.barcode) && ' (Verified)'}
              </li>
            ))}
          </ul>
        </div>
      )}

      {!allItemsVerified && (
        <BarcodeScanner onBarcodeScanned={handleBarcodeScanned} />
      )}

      {allItemsVerified && (
        <>
          <ShippingLabelGenerator order={selectedOrder} />
          <button onClick={handleFulfillOrder}>Complete Fulfillment</button>
        </>
      )}
    </div>
  );
};

export default FulfillmentPage;