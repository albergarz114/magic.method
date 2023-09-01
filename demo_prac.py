from typing import Any


class Beer:
    def __init__(self, name, type, price):
        self.name = name
        self.type = type
        self.price = price
    
    def __str__(self):
        return f"Name: {self.name}, Type: {self.type}, Price: {self.price}"
    
    def __repr__(self):
        return f"Beer({self.name} {self.type} {self.price})"
    
    def __eq__(self, other):
        if isinstance(other, Beer):
            return self.price == other.price
    
    def __lt__(self, other):
        if isinstance(other, Beer):
            return self.price < other.price
    
    def __getitem__(self, key):
        if key == "name":
            return self.name
        elif key == "type":
            return self.type
        elif key == "price":
            return self.price
        else:
            return None
    
    def __setitem__(self, key, value):
        if key == "name":
            self.name = value
        elif key == "type":
            self.type = value
        elif key == "price":
            self.type = value
        else:
            return None
    
    def __call__(self):
        return f"{self.type} is the type of beer"
    
    def __enter__(self):
        print(f"Entering...{self.name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Exiting...{self.name}")


beer1 = Beer("Budweiser", "Lager", 9.99)
beer2 = Beer("Coors Banquet", "Lager", 8.99)
beer3 = Beer("Coors Light", "Light Lager", 7.99)
print(beer1)
print(beer2)
print(beer3)
print(repr(beer1))
print(beer1 == beer2)
print(beer1 < beer2)

print(beer1["name"])
print(beer1["type"])
print(beer1["price"])
beer1.type = "IPA"
print(beer1["type"])
print(beer3())

