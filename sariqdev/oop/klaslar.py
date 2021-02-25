class Talaba:
    """Talaba nomli klass"""
    def __init__(self, ism, familiya, tyil):
        """Talabaning hususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil

    def get_name(self):
        """talabaning ismini qaytaradi"""
        return self.ism

    def get_lastname(self):
        """talabaning familiyasini qaytaradi"""
        return self.familiya

    def get_fullname(self):
        """Talabaningn ism familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"

    def get_age(self, yil):
        """talabaning yoshini qaytaradi"""
        return yil-self.tyil

    def tanishtir(self):
        print(f"ismim {self.ism} {self.familiya}. {self.tyil} da tug'ilganman")

talaba1 = Talaba('azizbek', 'tursunov', 2002) # talaba obyektini yaratdik
talaba2 = Talaba('nozima', 'shamsiddinova', 2003) # talaba obyektini yaratdik
talaba3 = Talaba('elon', 'mask', 2000) # talaba obyektini yaratdik

print(talaba2.get_age(2021))
talaba3.tanishtir()