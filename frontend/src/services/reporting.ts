import { createApiInstance } from 'frontend/src/services/api';

// HUMAN ASSISTANCE NEEDED
// The following functions have a confidence level below 0.8 and may need refinement for production use.
// Please review and adjust as necessary.

async function getInventoryReport(): Promise<any> {
  try {
    const api = createApiInstance();
    const response = await api.get('/reports/inventory');
    return response.data;
  } catch (error) {
    console.error('Error fetching inventory report:', error);
    throw error;
  }
}

async function getFulfillmentReport(): Promise<any> {
  try {
    const api = createApiInstance();
    const response = await api.get('/reports/fulfillment');
    return response.data;
  } catch (error) {
    console.error('Error fetching fulfillment report:', error);
    throw error;
  }
}

export { getInventoryReport, getFulfillmentReport };