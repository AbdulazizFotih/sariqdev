class Telefon:
    """Telefon haqida malumot beruvchi klass"""
    def __init__(self, model, brend, yil, narx):
        self.model = model
        self.brend = brend
        self.yil = yil
        self.narx = narx

    def get_info(self):
        return f"{self.brend}ning {self.model}nomli telefoni. {self.yil}-yilda ishlab chiqarilgan. Narxi: {self.narx} $"

tel1 = Telefon("Galaxy A30", 'Samsung', 2020, 500)
print(tel1.get_info())