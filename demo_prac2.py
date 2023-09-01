from typing import Any


class Shoes:
    def __init__(self, type, price):
        self.type = type
        self.price = price
    
    def __str__(self):
        return f"Type: {self.type}, Price: {self.price}"
    
    def __repr__(self):
        return f"Shoes({self.type} {self.price})"
    
    def __add__(self, other):
        if isinstance(other, Shoes):
            return self.price + other.price
        else:
            return None
    
    def __eq__(self, other):
        if isinstance(other, Shoes):
         return self.price == other.price
    
    def __lt__(self, other):
        if isinstance(other, Shoes):
            return self.price < other.price
    
    def __getitem__(self, key):
        if key == "type":
            return self.type
        elif key == "price":
            return self.price
        else:
            return None
        
    def __setitem__(self, key, value):
        if key == "type":
            self.type = value
        elif key == "price":
            self.price = value
        else:
            return None
        
    def __call__(self):
        return f"{self.type} is the type of shoes"
    
    def __enter__(self):
        print(f"Entering...{self.type}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Exiting...{self.type}")

shoes1 = Shoes("Nike", 99.99)
shoes2 = Shoes("Adidas", 89.99)
shoes3 = Shoes("Puma", 79.99)
print(shoes1)
print(shoes2)
print(shoes3)
print(repr(shoes1))
print(shoes1 == shoes2)
print(shoes1 < shoes2)

print(shoes1["type"])
print(shoes1["price"])
print(shoes2["type"])
print(shoes2["price"])
print(shoes3["type"])
print(shoes3["price"])

shoes1["type"] = "Nike Air"