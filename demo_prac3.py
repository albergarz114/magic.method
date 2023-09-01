class Cat:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Cat: {self.breed}, Name: {self.name}, Age: {self.age}"
    
    def __repr__(self):
        return f"Cat({self.breed} {self.name} {self.age})"
    
    def __add__(self, other):
        if isinstance(other, Cat):
            total_age = self.age + other.age
            return Cat(f"Total age: {total_age}", "Total age", total_age)
        return None
    
    def __eq__(self, other):
        if isinstance(other, Cat):
            return self.age == other.age
    
    def __lt__(self, other):
        if isinstance(other, Cat):
            return self.age < other.age
    
    def __getitem__(self, key):
        if key == "breed":
            return self.breed
        elif key == "name":
            return self.name
        elif key == "age":
            return self.age
        else:
            return None
        
    def __setitem__(self, key, value):
        if key == "breed":
            self.breed = value
        elif key == "name":
            self.name = value
        elif key == "age":
            self.age = value
        else:
            return None
        
    def __call__(self):
        return f"{self.breed} is the breed of cat"
    
    def __enter__(self):
        print(f"Entering...{self.breed}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Exiting...{self.breed}")


cat1 = Cat("Siamese", "Mittens", 3)
cat2 = Cat("Persian", "Fluffy", 5)
cat3 = Cat("Tabby", "Tiger", 2)
print(cat1)
print(cat2)
print(cat3)
print(repr(cat1))
added_age = cat1 + cat2
print(cat1 == cat2)
print(cat1 < cat2)

print(cat1["breed"])
print(cat1["name"])
print(cat1["age"])
cat1["breed"] = "Ragdoll"
print(cat1["breed"])
print(cat2["breed"])
print(cat3())
        
        