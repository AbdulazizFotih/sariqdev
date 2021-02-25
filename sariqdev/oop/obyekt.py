class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self, ism, familiya, tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya= familiya
        self.tyil = tyil
        self.bosqich = 1

    def get_info(self):
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi"

    def set_bosqich(self, bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = bosqich

# talaba0 = Talaba('azizbek', 'tursunov', 2002)
# print(talaba0.get_info())
# talaba0.bosqich= 4
# print(talaba0.get_info())

# talaba0.set_bosqich(3)
# print(talaba0.get_info())


class Fan:
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar