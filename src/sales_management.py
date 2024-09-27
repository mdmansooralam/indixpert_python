from src.sales import Sales


class SalesManagement(Sales):
    
    def add_sale(self, id, quantity):
        for product in self.inventory.products:
            if(product.id == id):
                stock = product.quantity
                if(quantity >stock):
                    print(f'Only {product.quantity} {product.name} is avalable')
                    break
                else:
                    self.all_sales_record.append(product)
                    product.quantity -= quantity
                    self.save_sales()
                    self.inventory.save_inventory()
                    print(f'{product.name} sold {quantity} and {product.quantity} in stock')
                    break
        else:
            print(f'product not found with ID : {id}')

    def view_sales(self, *arg):
        if(not arg):
            print('please enter the product ID or Name to view the sales')
        else:
            print('{:<10}{:<10}{:<20}{}'.format('Id', "Name", "Price", "Quantity"))
            for product in self.all_sales_record:
                if(product.id == arg[0] or product.name == arg[0]):
                    print('{:<10}{:>10}{:>20}{:>10}'.format(product.id, product.name, product.price, product.quantity))

    def view_all_sales(self):
         print('{:<10}{:<10}{:<20}{}'.format('Id', "Name", "Price", "Quantity"))
         for product in self.all_sales_record:
             print('{:<10}{:>10}{:>20}{:>10}'.format(product.id, product.name, product.price, product.quantity))