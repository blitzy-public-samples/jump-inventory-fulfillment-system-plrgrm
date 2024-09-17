import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import InventoryReport from 'frontend/src/components/Reporting/InventoryReport';
import FulfillmentReport from 'frontend/src/components/Reporting/FulfillmentReport';
import { getInventoryReport, getFulfillmentReport } from 'frontend/src/services/reporting';

// HUMAN ASSISTANCE NEEDED
// The following component may need additional refinement for production readiness.
// Please review and enhance error handling, loading states, and overall user experience.

const ReportingPage: React.FC = () => {
  const [activeTab, setActiveTab] = useState<'inventory' | 'fulfillment'>('inventory');
  const [startDate, setStartDate] = useState<Date>(new Date());
  const [endDate, setEndDate] = useState<Date>(new Date());
  const [reportData, setReportData] = useState<any>(null);

  const dispatch = useDispatch();

  const fetchReportData = async () => {
    try {
      if (activeTab === 'inventory') {
        const data = await getInventoryReport(startDate, endDate);
        setReportData(data);
      } else {
        const data = await getFulfillmentReport(startDate, endDate);
        setReportData(data);
      }
    } catch (error) {
      console.error('Error fetching report data:', error);
      // TODO: Implement proper error handling and user notification
    }
  };

  const handleTabChange = (tab: 'inventory' | 'fulfillment') => {
    setActiveTab(tab);
    setReportData(null);
  };

  const handleExport = () => {
    // TODO: Implement export functionality
    console.log('Export functionality not implemented yet');
  };

  return (
    <div className="reporting-page">
      <h1>Reports</h1>
      <div className="tabs">
        <button
          className={activeTab === 'inventory' ? 'active' : ''}
          onClick={() => handleTabChange('inventory')}
        >
          Inventory Report
        </button>
        <button
          className={activeTab === 'fulfillment' ? 'active' : ''}
          onClick={() => handleTabChange('fulfillment')}
        >
          Fulfillment Report
        </button>
      </div>
      <div className="date-range">
        <input
          type="date"
          value={startDate.toISOString().split('T')[0]}
          onChange={(e) => setStartDate(new Date(e.target.value))}
        />
        <input
          type="date"
          value={endDate.toISOString().split('T')[0]}
          onChange={(e) => setEndDate(new Date(e.target.value))}
        />
        <button onClick={fetchReportData}>Generate Report</button>
      </div>
      {reportData && (
        <div className="report-container">
          {activeTab === 'inventory' ? (
            <InventoryReport data={reportData} />
          ) : (
            <FulfillmentReport data={reportData} />
          )}
          <button onClick={handleExport}>Export Report</button>
        </div>
      )}
    </div>
  );
};

export default ReportingPage;