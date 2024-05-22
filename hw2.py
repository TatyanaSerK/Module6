class Vehicle:
    vehicle_type = "none"


class Car:
    price = 1000000

    def horse_powers(self, power):
        print('лошадинных сил -', power)


class Nissan(Vehicle, Car):
    vehicle_type = "внедорожник"
    price = 3500000

    def horse_powers(self, power):
        print('лошадинных сил -', power)


nis = Nissan()

print(nis.price)
print(nis.vehicle_type)