class Pantry:
    def __init__(self):
        self.items = {}

    def addItem(self, item, quantity):
        num = int(''.join(filter(str.isdigit, quantity)))
        if item in self.items:
            self.items[item] += num
        else:
            self.items[item] = num
        return True

    def removeItem(self, item, quantity):
        if item in self.items:
            num = int(''.join(filter(str.isdigit, quantity)))
            if self.items[item] <= num:
                del self.items[item]
            else:
                self.items[item] -= num
            return True
        else: 
            return False

    def getQuantity(self, item):
        return self.items.get(item, 0)
