import json
import os
from product import Product

SALES_FILE = 'sales.json'



from inventory import Inventory

class Sales:
    def __init__(self):
        self.all_sales_record = self.load_sales()
        self.inventory = Inventory()

    def load_sales(self):
        if(os.path.exists(SALES_FILE)):
            with open(SALES_FILE, 'r') as file:
                sales_record = json.load(file)
                return [Product(**sale) for sale in sales_record]
        return []
            
    def save_sales(self):
        with open(SALES_FILE, 'w') as file:
            sales_record = [sales.__dict__ for sales in self.all_sales_record]
            json.dump(sales_record, file, indent=4)


    