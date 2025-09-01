class InventoryManagement:
    def __init__(self):
        self.inventoryByStore = {}
        self.products = {} # productId -> Count
    
    def updateInventory(self, storeId, productId, count):
        if storeId not in self.inventoryByStore:
            self.inventoryByStore[storeId] = {}
        if productId not in self.inventoryByStore[storeId]:
            self.inventoryByStore[storeId][productId] = count
        else:
            self.inventoryByStore[storeId][productId] += count
        if productId not in self.products:
            self.products[productId] = count
        else:
            self.products[productId] += count
        
    def getStoreInventory(self, storeId):
        if storeId in self.inventoryByStore:
            return self.inventoryByStore[storeId]
        return {}
    
    def getTopSellingProduct(self, k:int):
        sortedProducts = sorted(self.products.items(), key=lambda x: x[1], reverse=True)
        return [productId for productId, count in sortedProducts[:k]]
    
# Example usage:
inventory = InventoryManagement()
inventory.updateInventory("store1", "productA", 10)
inventory.updateInventory("store1", "productB", 5)
inventory.updateInventory("store2", "productA", 3)
inventory.updateInventory("store2", "productC", 8)
print(inventory.getStoreInventory("store1"))  # {'productA': 10, 'productB': 5}
print(inventory.getTopSellingProduct(2))  # ['productA', 'productC']# Inventory Management System