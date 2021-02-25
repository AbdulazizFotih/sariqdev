class User:
    """Get user info""" 
    def __init__(self, ism, tyil, email):
        self.ism = ism
        self.tyil = tyil
        self.email= email
    
    def getinfo(self):
        print(f"Foydalanuvchi: {self.ism}, elektron pochta: {self.email}, tugilan yili: {self.tyil}")

user0 = User('azizbek', 2002, 'azizbektursunovofficial@gmail.com')

user0.getinfo()