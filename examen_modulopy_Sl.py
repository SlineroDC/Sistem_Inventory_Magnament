import time
import os 

def console_clear():
    os.system('clear')
#Create the display menu for after used in the loop

def display_menu():
    print("\nInventory Management System SL advisors")
    print("_"*50)
    print("1. Add Product")
    print("2. Search Product")
    print("3. Update Product Price")
    print("4. Delete Product")
    print("5. Calculate Total Inventory Value")
    print("6. Exit")
   
#Create to diccionary for saves the product
inventory = {
   
}

#Do you define the option of adding products we create the input for the entry a if to validate in the list if it is registered
#Return in case, but continues with the other product data within the tri (price value) to make it a character 
#Ensumeric we create with the data to enter the dictionary product.Inventory with the keys
#name, price,; we notify your income with a print and calling the values

def add_product1():
    
    console_clear()
    global inventory
    name = input("Insert the name of the product: ")
    if name in inventory:
        print("product existent.")
        return

    while True:
        try:
            price = float(input("Insert price: ")) 
            if price <= 0:
                print("error, must be greater than zero. ")  
            else:
                break
        except ValueError:
            print("error, the character must be numeric")
    
    while True:
        try:
            quantity = int(input("Insert the quantity: "))
            if quantity <= 0:
                print("error, must be greater than zero. ")
            else:    
                break
        except ValueError:
            print("error, the character must be numeric")
        
    inventory[name] = {
        "name": name,
        "price": price,
        "quantity": quantity,
    }

    print(f"Producto registrado: {name}, ${price:.2f}, Quantity: {quantity}")



# Function to search for a product by name
#With the cycle for we search the dictionary if it is touring it with the name
# but there is return. print name if be in dictionary
def search_product2():
    global inventory
    console_clear()
    if not inventory:
        print("\nInventario empty.")
        return
    name_product = input("Enter the product name to search: ").strip().lower()

    for name, data in inventory.items():
        if data["name"].strip().lower() == name_product:
            print("\n-------------- PRODUCT FOUND ---------------------")
            print(f"Name: {data['name']}")
            print(f"Price: ${data['price']:.2f}")
            print(f"Quantity: {data['quantity']}")
            break
    else:
        print("Product not found.")

# Function to update the price of an existing product
#we look for it with the cycle for first, if we are so we give the current price and check with a try the data type 
#and with an if that is positvo the value, we modify with the key in the dictionary

def update_product_price3():
    
    global inventory
    console_clear()

    if not inventory:
        print("\nInventory empty.")
        return

    print("\n--- INVENTORY ---")
    for name, data in inventory.items():
        print(f"{name}: ${data['price']:.2f}")

    price_to_change= input("Enter the product name to update price: ")

    if price_to_change not in inventory:
        print("Product not found.")
        return
    try:
        new_price = float(input("Enter the new price: "))
        if new_price ==0 or new_price<0:
            print("Error: The new price must be a positive number")
            return
        else:

            inventory[price_to_change]["price"] = new_price
            print(f"Update Price for {inventory[price_to_change]['price']}: ${new_price:.2f}")
    except ValueError:
        print("Invalid input. Price must be a number.")
        return


## Function to delete a product from the inventory
#we look for the product first, if etta we try to delete it 
# with a .pop calling it, but we return a print saying that it is not

def delete_product4():
    global inventory
    console_clear()

    if not inventory:
        print("Inventory empty.")            
        return

    print("\n--- INVENTORY ---")
    for name, data in inventory.items():
        print(f"{name}: ${data['price']:.2f})")

    while True:
        delete_product = input("Insert the name of the product to be removed: ")
        if delete_product in inventory:
            delete = inventory.pop(delete_product)
            print(f"Product delete: {delete['name']}")
            break
        else:
            print("Product not found")


#Function to calculate the total inventory value using lambda
#with the function map and sum up the key data and multiply them to obtain the total inventory

def calulate_Total_Inventory5():
    
    global inventory
    console_clear()

    if not inventory:
        print("\nInventory empty.")
        return

    total_value = sum(map(lambda data: data["price"] * data["quantity"], inventory.values()))
    print(f"Total inventory value: ${total_value:.2f}")


#option to get out of the menu loop and close the program
def exit():
    console_clear()
    print("Exiting the program, Goodbye!")


# Main program loop
while True:
        print("_"*50)
        display_menu()
        
        choice = input("Select an option 1-6: ")

        if choice == "1":
            add_product1()
        elif choice == "2":
            search_product2()
        elif choice == "3":
            update_product_price3()
        elif choice == "4":
            delete_product4()
        elif choice == "5":
            calulate_Total_Inventory5()
        elif choice == "6":
            exit()
            break
        else:
            print("Invalid option. Please select a number from 1 to 6 ")
        time.sleep(1)


        

