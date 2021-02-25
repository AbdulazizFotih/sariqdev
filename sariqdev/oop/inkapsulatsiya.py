from uuid import uuid4
class Avto:
    """Avtomabil klassi"""
    __num_avto = 0
    def __init__(self, make, model, rang, yil, narh, km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self, km):
        """Mashinaning km ga yana km qo'shish"""
        if km >= 0:
            self.__km += km
        else:
            print("mashina km kamaytirib bo'lmaydi!!!")

    @classmethod 
    def get_num_avto(cls):
        return cls.__num_avto

avto1 = Avto('Gm', 'Malibu', 'Qora', 2020, 40000, 100000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
# print(f'ID: {avto1.get_id()}')

# print(avto1.get_km()) # oldin
# avto1.add_km(1500) # km qo'shish
# print(avto1.get_km()) # keyin

print(Avto.get_num_avto())