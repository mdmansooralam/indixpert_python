from src.inventory_management import InventoryManagement

class ManageInventory(InventoryManagement):
    
    def add(self):
        try:
            name = input("Product Name : ")
            if(name == "" or name == '-1'):
                raise ValueError ('enter a valid product name')
            
            price = float(input('Price : '))
            if(price <0):
                raise ValueError ('please enter a valid price')
            
            quantity = int(input("Quantity : "))
            if(quantity <0):
                raise ValueError ('please enter a valid quantity')
            
            self.add_product(name, quantity, price)

        except:
            print('Please enter a valid data')

    def update(self):
        #need id, name, quantity, price
        pass

    def delete(self):
        #need id
        pass
    
    def restock(self):
        #need id quantity
        pass

    def search(self):
        #need id
        pass

    def view_all_product():
        #blank
        pass

    def sale(self):
        #need id, quantity
        pass

    def view_sale(self):
        #need id
        pass

    def view_all_sales(self):
        # blank
        pass

        