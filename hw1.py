class Car:
    price = 1000
    def horse_powers(self):
        print('лошадинных сил 500' )


class Nissan(Car):
    price = 2000
    def horse_powers(self):
        print('лошадинных сил-200')

class Kia(Car):
    price = 1555
    def horse_powers(self):
        print('лошадинных сил-180')

kia = Kia()
kia.horse_powers()
print('стоимость КИА', Kia.price)

nis = Nissan()
nis.horse_powers()
print('стоимость Ниссан',Nissan.price)