import { z } from 'zod';

export interface Product {
  id: string;
  name: string;
  description: string;
  sku: string;
  quantity: number;
  price: number;
}

export const productSchema = z.object({
  id: z.string(),
  name: z.string(),
  description: z.string(),
  sku: z.string(),
  quantity: z.number(),
  price: z.number()
});

// HUMAN ASSISTANCE NEEDED
// Please review the productSchema to ensure it meets all requirements.
// Consider adding additional validation rules if necessary, such as:
// - Minimum length for strings
// - Positive number validation for quantity and price
// - Any specific format requirements for SKU