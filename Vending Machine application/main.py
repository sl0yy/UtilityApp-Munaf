from Items_Config import setup_vending_machine

def display_menu(vm, category=None):
    """Display the vending machine menu, optionally filtered by category."""
    print("\nVending Machine Menu:")
    if category:
        print(f"Category: {category.capitalize()}")
    for product in vm.productList.values():
        if category is None or product.typeOfItem.lower() == category.lower():
            availability = "Available" if product.isAvailable() else "Out of Stock"
            print(f"{product.idCode} - {product.title} ({product.typeOfItem}): ${product.cost:.2f} [{availability}]")
    print("\n")

def main():
    vending_machine = setup_vending_machine()

    while True:
        print("\nWelcome to the Vending Machine!")
        print("1. View Full Menu")
        print("2. View Drinks Menu")
        print("3. View Sweets Menu") 
        print("4. Get Change and Exit")

        choice = input("Enter your choice: ").strip()

        if choice in ["1", "2", "3"]:
            # Show the menu based on choice
            if choice == "1":
                display_menu(vending_machine)
            elif choice == "2":
                display_menu(vending_machine, category="Drinks")
            elif choice == "3":
                display_menu(vending_machine, category="Snacks")

            # Ask how much the user wants to deposit
            try:
                amount = float(input("How much would you like to deposit? "))
                if amount <= 0:
                    print("Amount must be greater than zero.")
                    continue
                else:
                    vending_machine.depositMoney(amount)
                    print(f"Current Balance: ${vending_machine.currentBalance:.2f}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            # Ask for the product code
            code = input("Enter the product code: ").strip()
            product = vending_machine.findProduct(code)
            if product:
                if product.isAvailable():
                    success, remaining = vending_machine.processPurchase(product)
                    if success:
                        print(f"Purchased {product.title} for ${product.cost:.2f}. Remaining balance: ${remaining:.2f}")
                    else:
                        print(f"Insufficient balance! You need ${remaining:.2f} more.")
                else:
                    print(f"{product.title} is out of stock.")
            else:
                print("Invalid product code. Please try again.")

        elif choice == "4":
            change = vending_machine.getChange()
            print(f"Here is your change: ${change:.2f}. Thank you for using the vending machine!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()




