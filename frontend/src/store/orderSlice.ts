import { createSlice, PayloadAction, createAsyncThunk } from '@reduxjs/toolkit';
import { getUnfulfilledOrders, fulfillOrder } from 'frontend/src/services/orders';
import { Order } from 'frontend/src/schema/order';

interface OrderState {
  unfulfilledOrders: Order[];
  loading: boolean;
  error: string | null;
}

const initialState: OrderState = {
  unfulfilledOrders: [],
  loading: false,
  error: null,
};

// HUMAN ASSISTANCE NEEDED
// The fetchUnfulfilledOrdersThunk and fulfillOrderThunk functions need to be implemented
// with proper error handling and state updates. The confidence level for these functions is below 0.8.

export const fetchUnfulfilledOrdersThunk = createAsyncThunk(
  'order/fetchUnfulfilled',
  async (_, { rejectWithValue }) => {
    try {
      const orders = await getUnfulfilledOrders();
      return orders;
    } catch (error) {
      return rejectWithValue('Failed to fetch unfulfilled orders');
    }
  }
);

export const fulfillOrderThunk = createAsyncThunk(
  'order/fulfill',
  async (orderId: string, { rejectWithValue }) => {
    try {
      await fulfillOrder(orderId);
      return orderId;
    } catch (error) {
      return rejectWithValue('Failed to fulfill order');
    }
  }
);

const orderSlice = createSlice({
  name: 'order',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchUnfulfilledOrdersThunk.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchUnfulfilledOrdersThunk.fulfilled, (state, action: PayloadAction<Order[]>) => {
        state.loading = false;
        state.unfulfilledOrders = action.payload;
      })
      .addCase(fetchUnfulfilledOrdersThunk.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload as string;
      })
      .addCase(fulfillOrderThunk.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fulfillOrderThunk.fulfilled, (state, action: PayloadAction<string>) => {
        state.loading = false;
        state.unfulfilledOrders = state.unfulfilledOrders.filter(order => order.id !== action.payload);
      })
      .addCase(fulfillOrderThunk.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload as string;
      });
  },
});

export default orderSlice.reducer;