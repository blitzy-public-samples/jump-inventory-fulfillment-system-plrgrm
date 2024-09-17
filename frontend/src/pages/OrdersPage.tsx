// HUMAN ASSISTANCE NEEDED
// The confidence level is below 0.8, so this code may need further review and adjustments for production readiness.

import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import OrderList from 'frontend/src/components/OrderManagement/OrderList';
import OrderDetails from 'frontend/src/components/OrderManagement/OrderDetails';
import { fetchUnfulfilledOrdersThunk, fulfillOrderThunk } from 'frontend/src/store/orderSlice';

const OrdersPage: React.FC = () => {
  const [activeTab, setActiveTab] = useState<'unfulfilled' | 'fulfillable'>('unfulfilled');
  const [selectedOrder, setSelectedOrder] = useState<string | null>(null);
  
  const dispatch = useDispatch();
  const orders = useSelector((state: any) => state.orders.unfulfilledOrders);
  const fulfillableOrders = useSelector((state: any) => state.orders.fulfillableOrders);

  useEffect(() => {
    dispatch(fetchUnfulfilledOrdersThunk());
  }, [dispatch]);

  const handleOrderSelect = (orderId: string) => {
    setSelectedOrder(orderId);
  };

  const handleFulfillOrder = (orderId: string) => {
    dispatch(fulfillOrderThunk(orderId));
    setSelectedOrder(null);
  };

  return (
    <div className="orders-page">
      <div className="tabs">
        <button
          className={activeTab === 'unfulfilled' ? 'active' : ''}
          onClick={() => setActiveTab('unfulfilled')}
        >
          Unfulfilled Orders
        </button>
        <button
          className={activeTab === 'fulfillable' ? 'active' : ''}
          onClick={() => setActiveTab('fulfillable')}
        >
          Orders That Can Be Fulfilled
        </button>
      </div>

      <div className="order-management">
        <OrderList
          orders={activeTab === 'unfulfilled' ? orders : fulfillableOrders}
          onSelectOrder={handleOrderSelect}
        />
        {selectedOrder && (
          <OrderDetails
            order={orders.find((order: any) => order.id === selectedOrder) || 
                   fulfillableOrders.find((order: any) => order.id === selectedOrder)}
            onFulfillOrder={handleFulfillOrder}
          />
        )}
      </div>
    </div>
  );
};

export default OrdersPage;