# Amir Abu Hani

class Items:
    total_weight = 0
    total_items = 0

    def __init__(self, weight):
        self.weight = int(weight)
        Items.total_weight = self.weight


class UniversalCharger(Items):
    def __init__(self, color, price, size, brand, weight):
        super().__init__(weight)
        self.color = color
        self.price = price
        self.size = size
        self.brand = brand

    def print_item(self):
        return {
            "Color": self.color,
            "Price": self.price,
            "Size": self.size,
            "Brand": self.brand,
            "weight": self.weight
        }


class Passport(Items):
    def __init__(self, color, weight, cost, boughtFrom):
        super().__init__(weight)
        self.color = color
        self.cost = cost
        self.boughtFrom = boughtFrom

    def print_item(self):
        return {
            "color": self.color,
            "weight": self.weight,
            "cost": self.cost,
            "bought from": self.boughtFrom
        }


class Sunglasses(Items):
    def __init__(self, haveCase, color, origin, weight):
        super().__init__(weight)
        self.haveCase = haveCase
        self.color = color
        self.origin = origin

    def print_item(self):
        return {
            "have case": self.haveCase,
            "color": self.color,
            "origin": self.origin,
            "weight": self.weight
        }


class Sneakers(Items):
    def __init__(self, brand, new, boughtFrom, weight):
        super().__init__(weight)
        self.brand = brand
        self.new = new
        self.boughtFrom = boughtFrom

    def print_item(self):
        return {
            "brand": self.brand,
            "new": self.new,
            "bought From": self.boughtFrom,
            "weight": self.weight
        }


class Smartphone(Items):
    def __init__(self, brand, operating_system, storage, display, camera, materials, weight):
        super().__init__(weight)
        self.brand = brand
        self.operating_system = operating_system
        self.storage = storage
        self.display = display
        self.camera = camera
        self.materials = materials

    def print_item(self):
        return {
            "brand": self.brand,
            "operating system": self.operating_system,
            "storage": self.storage,
            "display": self.display,
            "camera": self.camera,
            "materials": self.materials,
            "weight": self.weight
        }


class Laptop(Items):
    def __init__(self, brand, processor, ram, storage, graphics, weight):
        super().__init__(weight)
        self.brand = brand
        self.processor = processor
        self.ram = ram
        self.storage = storage
        self.graphics = graphics

    def print_item(self):
        return {
            "brand": self.brand,
            "processor": self.processor,
            "ram": self.ram,
            "storage": self.storage,
            "graphics": self.graphics,
            "weight": self.weight
        }


class Smartwatch(Items):
    def __init__(self, brand, display, battery_life, fitness_features, connectivity, weight):
        super().__init__(weight)
        self.brand = brand
        self.display = display
        self.battery_life = battery_life
        self.fitness_features = fitness_features
        self.connectivity = connectivity

    def print_item(self):
        return {
            "brand": self.brand,
            "display": self.display,
            "battery life": self.battery_life,
            "fitness features": self.fitness_features,
            "connectivity": self.connectivity,
            "weight": self.weight
        }


class Campus(Items):
    def __init__(self, brand, accuracy, price, materials, weight):
        super().__init__(weight)
        self.brand = brand
        self.accuracy = accuracy
        self.price = price
        self.materials = materials

    def print_item(self):
        return {
            "brand": self.brand,
            "accuracy": self.accuracy,
            "price": self.price,
            "materials": self.materials,
            "weight": self.weight
        }


class Bag:
    def __init__(self):
        self.bag = []

    def add_item(self, item):
        item_name = item.__class__.__name__
        if Items.total_weight <= 80 and Items.total_items < 6:
            self.bag.append(item)
            print(f"{item_name} has been successfully added to the bag.")
            Items.total_weight += item.weight
            Items.total_items += 1
            print(f"The number of items in the bag is: {Items.total_items}")
        elif Items.total_weight > 80:
            print(f"Cannot adding {item_name}. Total weight exceeds 80.")
        else:
            print(f"Cannot adding {item_name}. Total number of items exceeds 6.")

    def remove_item(self, item):
        item_name = item.__class__.__name__
        if item in self.bag:
            self.bag.remove(item)
            print(f"{item_name}  has been successfully removed from the bag.")
            Items.total_weight -= item.weight
            Items.total_items -= 1
            print(f"The number of items in the bag is: {Items.total_items}")
        else:
            print(f"{item_name} not found in the bag.")

    def get_info_items(self):
        if self.bag:
            for item in self.bag:
                info = item.print_item()
                print(item.__class__.__name__)
                for key, value in info.items():
                    print(f"{key}: {value}")
                print()
        else:
            print("The bag is empty!")


UniversalCharger = UniversalCharger("Black", "50", "Medium", "Lenovo", 12)
passport = Passport("blue", 1, "50", "USA")
sunglasses = Sunglasses("yes", "black", "Italy", 10)
sneakers = Sneakers("New Balance", False, "Spain", 14)
smartphone = Smartphone("Apple", "iOS", "128 GB", "AMOLED", "Daul Lens", "lithium, plastic", 30)
laptop = Laptop("Dell", "Intel i7", "16 GB", "512 GB SSD", "NVIDIA GeForce4", 60)
smartwatch = Smartwatch("Samsung", "Touchscreen", "3 days", "Heart Rate Monitor", "Bluetooth", 44)
campus = Campus("Samsung", "high", "50", "iron, plastic", 4)
my_bag = Bag()

while True:
    user_choice = input("Do you want to add or remove an item? (add/remove/quit): ")
    if user_choice == "add":
        item_type = input("Which item do you want to add? (universal charger/passport/sunglasses/sneakers/smartphone/"
                          "laptop/smartwatch/campus): ")
        if item_type == "universal charger":
            my_bag.add_item(UniversalCharger)
        elif item_type == "passport":
            my_bag.add_item(passport)
        elif item_type == "sunglasses":
            my_bag.add_item(sunglasses)
        elif item_type == "sneakers":
            my_bag.add_item(sneakers)
        elif item_type == "smartphone":
           my_bag.add_item(smartphone)
        elif item_type == "laptop":
            my_bag.add_item(laptop)
        elif item_type == "smartwatch":
            my_bag.add_item(smartwatch)
        elif item_type == "campus":
                my_bag.add_item(campus)

        else:
            print("Invalid item type!")
    elif user_choice == "remove":
        item_type = input("Which item do you want to remove?  ("
                          "universal charger/passport/sunglasses/sneakers/smartphone/"
                          "laptop/smartwatch/campus): ")
        if item_type == "universal charger":
            my_bag.remove_item(UniversalCharger)
        elif item_type == "passport":
            my_bag.remove_item(passport)
        elif item_type == "sunglasses":
            my_bag.remove_item(sunglasses)
        elif item_type == "sneakers":
            my_bag.remove_item(sneakers)
        elif item_type == "smartphone":
                my_bag.remove_item(smartphone)
        elif item_type == "laptop":
            my_bag.remove_item(laptop)
        elif item_type == "smartwatch":
            my_bag.remove_item(smartwatch)
        elif item_type == "campus":
            my_bag.remove_item(campus)
        else:
            print("Invalid item type!")
    elif user_choice == "quit":
        break
    else:
        print("Invalid choice!")

print("Items in the bag:")
my_bag.get_info_items()
