import { createApiInstance } from 'frontend/src/services/api';
import { Order, OrderSchema } from 'frontend/src/schema/order';

// HUMAN ASSISTANCE NEEDED
// The following function may need additional error handling and edge case management
export async function getUnfulfilledOrders(): Promise<Order[]> {
  const api = createApiInstance();
  try {
    const response = await api.get('/orders/unfulfilled');
    const validatedOrders = OrderSchema.array().parse(response.data);
    return validatedOrders;
  } catch (error) {
    console.error('Error fetching unfulfilled orders:', error);
    throw error;
  }
}

// HUMAN ASSISTANCE NEEDED
// This function needs more robust error handling and possibly a more detailed response
export async function fulfillOrder(orderId: string): Promise<boolean> {
  const api = createApiInstance();
  try {
    const response = await api.post(`/orders/${orderId}/fulfill`);
    return response.status === 200;
  } catch (error) {
    console.error(`Error fulfilling order ${orderId}:`, error);
    return false;
  }
}