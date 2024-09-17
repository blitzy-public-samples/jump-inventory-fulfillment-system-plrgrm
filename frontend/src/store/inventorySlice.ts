import { createSlice, PayloadAction, createAsyncThunk } from '@reduxjs/toolkit';
import { getInventory, updateInventory } from 'frontend/src/services/inventory';
import { Product } from 'frontend/src/schema/product';

interface InventoryState {
  products: Product[];
  loading: boolean;
  error: string | null;
}

const initialState: InventoryState = {
  products: [],
  loading: false,
  error: null,
};

// HUMAN ASSISTANCE NEEDED
// The fetchInventoryThunk and updateInventoryThunk functions have lower confidence levels.
// Please review and adjust as necessary.

export const fetchInventoryThunk = createAsyncThunk(
  'inventory/fetchInventory',
  async (_, { rejectWithValue }) => {
    try {
      const inventory = await getInventory();
      return inventory;
    } catch (error) {
      return rejectWithValue('Failed to fetch inventory');
    }
  }
);

export const updateInventoryThunk = createAsyncThunk(
  'inventory/updateInventory',
  async (updatedProducts: Product[], { rejectWithValue }) => {
    try {
      await updateInventory(updatedProducts);
      return updatedProducts;
    } catch (error) {
      return rejectWithValue('Failed to update inventory');
    }
  }
);

const inventorySlice = createSlice({
  name: 'inventory',
  initialState,
  reducers: {
    setInventory: (state, action: PayloadAction<Product[]>) => {
      state.products = action.payload;
    },
    updateProductQuantities: (state, action: PayloadAction<Product[]>) => {
      action.payload.forEach(updatedProduct => {
        const index = state.products.findIndex(p => p.id === updatedProduct.id);
        if (index !== -1) {
          state.products[index].quantity = updatedProduct.quantity;
        }
      });
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchInventoryThunk.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchInventoryThunk.fulfilled, (state, action) => {
        state.loading = false;
        state.products = action.payload;
      })
      .addCase(fetchInventoryThunk.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload as string;
      })
      .addCase(updateInventoryThunk.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(updateInventoryThunk.fulfilled, (state, action) => {
        state.loading = false;
        state.products = action.payload;
      })
      .addCase(updateInventoryThunk.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload as string;
      });
  },
});

export const { setInventory, updateProductQuantities } = inventorySlice.actions;
export default inventorySlice.reducer;