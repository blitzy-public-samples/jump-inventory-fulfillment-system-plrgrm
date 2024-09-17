import { z } from 'zod';

// Interfaces
export interface OrderItem {
  product_id: string;
  sku: string;
  name: string;
  quantity: number;
  price: number;
}

export interface Order {
  id: string;
  shopify_order_id: string;
  status: string;
  order_date: Date;
  items: OrderItem[];
  customer_name: string;
  shipping_address: string;
  total_amount: number;
}

// HUMAN ASSISTANCE NEEDED
// The following schemas have a confidence level below 0.8 and may need review or adjustments
// Zod schemas
export const orderItemSchema = z.object({
  product_id: z.string(),
  sku: z.string(),
  name: z.string(),
  quantity: z.number().int().positive(),
  price: z.number().positive()
});

export const orderSchema = z.object({
  id: z.string(),
  shopify_order_id: z.string(),
  status: z.string(),
  order_date: z.date(),
  items: z.array(orderItemSchema),
  customer_name: z.string(),
  shipping_address: z.string(),
  total_amount: z.number().positive()
});