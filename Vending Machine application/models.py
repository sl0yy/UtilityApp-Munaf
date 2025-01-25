class Product:
    """Represents a product inside the vending machine."""
    def __init__(self, idCode, title, typeOfItem, cost, quantity):
        self.idCode = idCode
        self.title = title
        self.typeOfItem = typeOfItem
        self.cost = cost
        self.quantity = quantity

    def isAvailable(self):
        """Returns True if the product is available for purchase."""
        return self.quantity > 0

    def vend(self): 
        """Decrease the stock after a product is purchased."""
        if self.isAvailable():
            self.quantity -= 1
            return True
        return False


class VendingSystem:
    """Handles the operations of the vending machine."""
    def __init__(self):
        self.productList = {}
        self.currentBalance = 0.0

    def addProduct(self, product):
        """Adds a new product to the vending machine."""
        self.productList[product.idCode] = product

    def findProduct(self, idCode):
        """Find and return a product using its unique identifier."""
        return self.productList.get(idCode)

    def depositMoney(self, amount):
        """Add funds to the machine's current balance."""
        self.currentBalance += amount

    def processPurchase(self, product):
        """Handles the purchase transaction for a product."""
        if self.currentBalance >= product.cost:
            self.currentBalance -= product.cost
            product.vend()
            return True, self.currentBalance
        return False, product.cost - self.currentBalance

    def getChange(self):
        """Returns the leftover balance after a transaction."""
        change = self.currentBalance
        self.currentBalance = 0.0
        return change
