from models import Product, VendingSystem

def setup_vending_machine():
    """Configure the vending machine with items."""
    vm = VendingSystem()
    vm.addProduct(Product("A1", "Biscuit", "Snacks", 1.50, 10))
    vm.addProduct(Product("A2", "Chocolate", "Snacks", 1.40, 5))
    vm.addProduct(Product("A3", "Popcorn", "Snacks", 1.20, 8))
    vm.addProduct(Product("A4", "Dry Fruit", "Snacks", 1.30, 2)) 
    vm.addProduct(Product("A5", "Ice cream", "Snacks", 2.00, 7))
    vm.addProduct(Product("A6", "Sandwich", "Snacks", 2.50, 10))
    vm.addProduct(Product("A7", "Sweets", "Snacks", 2.50, 0))

    vm.addProduct(Product("C1", "Lemon Drink", "Drinks", 2.50, 10))
    vm.addProduct(Product("C2", "Water", "Drinks", 2.50, 10))
    vm.addProduct(Product("C3", "Latte", "Drinks", 2.50, 10))
    vm.addProduct(Product("C4", "Juice", "Drinks", 2.50, 10))
    vm.addProduct(Product("C5", "Ice Tea", "Drinks", 2.50, 10))
    return vm
