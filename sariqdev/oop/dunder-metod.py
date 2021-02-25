class Avto:
    __num_avto = 0
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narh):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1

    def __repr__(self):
        """Obyekt haqida malumot"""
        return f"Avto: {self.rang} {self.make} {self.model}"

    def __eq__(self, boshqa_avto):
        """tenglik"""
        return self.narh == boshqa_avto.narh

    def __lt__(self, boshqa_avto):
        """kichik"""
        return self.narh<boshqa_avto

    def __le__(self, boshqa_avto):
        """Kichik yoki teng"""
        return self.narh <= boshqa_avto.narh

avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
print(avto1>avto2)
