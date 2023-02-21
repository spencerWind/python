class User:
    def __init__(self) -> None:
        self.first_name = 'Spencer'
        self.last_name = 'Wind'
        self.age = 19
        self.shoe_size = 9.5

    def announce_shoe_size(self):
        print(f'Hello! My name is {self.first_name} and I wear a size {self.shoe_size}')

spencer_wind = User()

print(spencer_wind.first_name)

ike_burnside = User()

print(ike_burnside.first_name)

ike_burnside.first_name = 'Isaac'
ike_burnside.last_name = 'Burnside'
ike_burnside.age = 22
ike_burnside.shoe_size = 12

print(ike_burnside.first_name)

class Shoe:
    def __init__(self, brand, model, type, price) -> None:
        self.brand = brand
        self.model = model
        self.type = type
        self.price = price
        self.stock = True

    def update_price(self, new_price):
        self.price = new_price

nike_af1 = Shoe('Nike','Air Force 1','Low Top Sneaker',110)

print(nike_af1.price)
print(nike_af1.stock)
spencer_wind.announce_shoe_size()

vans_sk8_h1 = Shoe('Vans','Skate Hi','High Top Skate Shoe',70)
print(vans_sk8_h1.price)

vans_sk8_h1.update_price(80)
print(vans_sk8_h1.price)