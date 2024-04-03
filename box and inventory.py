class Sword():
    def __init__ (self, damage, weight):
        self.damage = damage
        self.weight = weight

class Bow():
    def __init__ (self,renge, price):
        self.renge = renge
        self.price = price
        
class Chestplate():
    def __init__ (self, protection, block):
        self.protection = protection
        self.block = block
        
class Chest():
    def __init__ (self):
        self.items = []
        
    def open_chest (self):
        for item in self.items:
            print(item.__dict__)
            
    def put(self, object):
        self.items.append(object)
    
    def delete(self,object):
        self.items.remove(object)
    
class Inventory():
    def __init__(self):
        self.items = []
    
    def open_inventory (self):
        for item in self.items:
            print(item.__dict__)
            
    def put(self, object):
        self.items.append(object)
        
Sword1 = Sword(39, 19)
Bow1 = Bow(60, 100)
Chestplate1 = Chestplate(49, 35)

box = Chest()
inv = Inventory()

box.put(Sword1)
box.put(Bow1)
box.put(Chestplate1)
box.delete(Sword1)

box.open_chest()

inv.put(Sword1)

inv.open_inventory()
