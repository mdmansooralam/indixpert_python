
from src.utils.manage_inventory import ManageInventory

def main():
    inventory = ManageInventory()
    while True:
        print(f'1 add product')
        print(f'2 update product')
        print(f'3 delete product')
        print(f'4 search product')
        print(f'4 view all product')
        print(f'4 add stock')
        print(f'10 exit')

        choice = input('please choose Option Which is givn above : ')
        if(choice == '1'):
            inventory.add()
            continue
        elif(choice == '2'):
            pass
        elif(choice == 10):
            break
        else:
            print("Please choose a valid option")

    
if __name__ == "__main__":
    main()