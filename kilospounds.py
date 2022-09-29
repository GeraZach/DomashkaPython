class Pounds:
    def __init__(self, kilos):
        self.kilos = kilos * 2.2


kilosToPounds = Pounds(20)

print(kilosToPounds.kilos)


class Kilos:
    def __init__(self, pounds):
        self.pounds = pounds / 2.2


poundsToKilos = Kilos(100)

print(poundsToKilos.pounds)
