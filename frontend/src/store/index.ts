import { configureStore } from '@reduxjs/toolkit';
import { authReducer } from './authSlice';
import { orderReducer } from './orderSlice';
import { inventoryReducer } from './inventorySlice';

const configureAppStore = () => {
  return configureStore({
    reducer: {
      auth: authReducer,
      order: orderReducer,
      inventory: inventoryReducer,
    },
    // Add any middleware here if needed
  });
};

export type RootState = ReturnType<ReturnType<typeof configureAppStore>['getState']>;
export type AppDispatch = ReturnType<typeof configureAppStore>['dispatch'];

export default configureAppStore;