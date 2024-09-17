import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import OrderSummary from 'frontend/src/components/Dashboard/OrderSummary';
import InventorySummary from 'frontend/src/components/Dashboard/InventorySummary';
import RecentActivity from 'frontend/src/components/Dashboard/RecentActivity';
import { fetchUnfulfilledOrdersThunk } from 'frontend/src/store/orderSlice';
import { fetchInventoryThunk } from 'frontend/src/store/inventorySlice';

const DashboardPage: React.FC = () => {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(fetchUnfulfilledOrdersThunk());
    dispatch(fetchInventoryThunk());
  }, [dispatch]);

  return (
    <div className="dashboard-page">
      <h1>Dashboard</h1>
      <div className="dashboard-content">
        <OrderSummary />
        <InventorySummary />
        <RecentActivity />
      </div>
    </div>
  );
};

export default DashboardPage;