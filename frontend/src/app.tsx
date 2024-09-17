import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import ProtectedRoute from './components/Auth/ProtectedRoute';
import DashboardPage from './pages/DashboardPage';
import OrdersPage from './pages/OrdersPage';
import InventoryPage from './pages/InventoryPage';
import FulfillmentPage from './pages/FulfillmentPage';
import ReportingPage from './pages/ReportingPage';
import Login from './components/Auth/Login';

const App: React.FC = () => {
  return (
    <BrowserRouter>
      <div className="app-container">
        <header>
          {/* Add header content here */}
        </header>
        <main>
          <Routes>
            <Route path="/login" element={<Login />} />
            <Route path="/" element={<ProtectedRoute><DashboardPage /></ProtectedRoute>} />
            <Route path="/orders" element={<ProtectedRoute><OrdersPage /></ProtectedRoute>} />
            <Route path="/inventory" element={<ProtectedRoute><InventoryPage /></ProtectedRoute>} />
            <Route path="/fulfillment" element={<ProtectedRoute><FulfillmentPage /></ProtectedRoute>} />
            <Route path="/reporting" element={<ProtectedRoute><ReportingPage /></ProtectedRoute>} />
          </Routes>
        </main>
        <footer>
          {/* Add footer content here */}
        </footer>
      </div>
    </BrowserRouter>
  );
};

export default App;