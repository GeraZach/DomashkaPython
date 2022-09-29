class ConvertWeight:
    def __init__(self, pounds):
        self.pounds = pounds / 2.2

    def calc(self):
        return int(self.pounds)


Kilos = ConvertWeight(int(input('How many pounds of white powder u want?')))
print('Pounds to kilos converted: ')
print(Kilos.calc(), 'kilos')


class Price:
    def __init__(self, kilos):
        self.kilos = kilos

    def price(self):
        return self.kilos * 33


PowderPrice = Price(int(Kilos.calc()))
print('Price: ')
print(PowderPrice.price(), 'mil')
