"""
Shopping Cart
Create a list of products.

Allow the user to:

Add products.
Remove products.
Display all products.
Show total number of products.
"""
products = []

print("--- Welcome to the Shopping Cart ---")

while True:
    print('\nList of operations allowed:')
    print('1. Add product')
    print('2. Remove product')
    print('3. Display all products')
    print('4. Show total number of products')
    print('5. Exit')
    
    choose = input("\nChoose any number from 1 to 5: ")

    if choose == '1':
        product = input("Enter the name of the product you want to add: ").strip()
        if product:
            products.append(product)
            print(f"'{product}' has been added.")
        else:
            print("Product name cannot be empty!")

    elif choose == '2':
        product = input("Enter the name of the product you want to remove: ").strip()
        # Safety check: make sure the item actually exists before removing it
        if product in products:
            products.remove(product)
            print(f"'{product}' has been removed.")
        else:
            print(f"Error: '{product}' is not in your shopping cart.")

    elif choose == '3':
        if products:
            print("\nYour Current Shopping Cart:")
            for index, item in enumerate(products, 1):
                print(f"{index}. {item}")
        else:
            print("\nYour shopping cart is currently empty.")

    elif choose == '4':
        print(f'\nThe total number of products is: {len(products)}')

    elif choose == '5':
        print("Exiting program. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please select a number between 1 and 5.")