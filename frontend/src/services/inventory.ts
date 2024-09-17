import { createApiInstance } from 'frontend/src/services/api';
import { Product, ProductSchema } from 'frontend/src/schema/product';

// HUMAN ASSISTANCE NEEDED
// The following function has a confidence level of 0.7 and may need review
export async function getInventory(): Promise<Product[]> {
  try {
    const api = createApiInstance();
    const response = await api.get('/inventory');
    
    // Validate and parse the response
    const validatedData = ProductSchema.array().parse(response.data);
    
    return validatedData;
  } catch (error) {
    console.error('Error fetching inventory:', error);
    throw new Error('Failed to fetch inventory');
  }
}

// HUMAN ASSISTANCE NEEDED
// The following function has a confidence level of 0.6 and may need review
export async function updateInventory(updatedProducts: Product[]): Promise<boolean> {
  try {
    const api = createApiInstance();
    const response = await api.put('/inventory', updatedProducts);
    
    // Assuming the API returns a success status
    return response.status === 200;
  } catch (error) {
    console.error('Error updating inventory:', error);
    return false;
  }
}