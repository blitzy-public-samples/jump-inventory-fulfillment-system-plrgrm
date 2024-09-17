import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import InventoryList from 'frontend/src/components/InventoryManagement/InventoryList';
import InventoryUpdate from 'frontend/src/components/InventoryManagement/InventoryUpdate';
import { fetchInventoryThunk, updateInventoryThunk } from 'frontend/src/store/inventorySlice';

// HUMAN ASSISTANCE NEEDED
// The confidence level is below 0.8, so this component may need review and improvements.
// Additionally, we're adding useEffect to the imports as it's needed for fetching data on mount.

const InventoryPage: React.FC = () => {
  const dispatch = useDispatch();
  const inventory = useSelector((state: RootState) => state.inventory.items);
  const [selectedProduct, setSelectedProduct] = useState<Product | null>(null);

  useEffect(() => {
    dispatch(fetchInventoryThunk());
  }, [dispatch]);

  const handleProductSelect = (product: Product) => {
    setSelectedProduct(product);
  };

  const handleInventoryUpdate = (productId: string, newQuantity: number) => {
    dispatch(updateInventoryThunk({ productId, quantity: newQuantity }));
    setSelectedProduct(null);
  };

  return (
    <div className="inventory-page">
      <h1>Inventory Management</h1>
      <InventoryList 
        inventory={inventory} 
        onProductSelect={handleProductSelect} 
      />
      {selectedProduct && (
        <InventoryUpdate 
          product={selectedProduct} 
          onUpdate={handleInventoryUpdate} 
        />
      )}
    </div>
  );
};

export default InventoryPage;