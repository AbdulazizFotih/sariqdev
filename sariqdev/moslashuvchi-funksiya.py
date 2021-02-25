############ *args

# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi

# print(summa(5, 5))

# def summa1(*sonla):
#     """Kiritilgan sonlar yigindisini hisoblaydigan funksiya"""
#     return sum(sonla)

# print(summa1(4, 5, 6, 7))


######## **kwargs ##########

def avto_info(kompaniya, model, **malumot):
    """Avto haqida malumot beradigan lugat ko'rinishini qaytaruvchi funksiya"""
    malumot['kompaniya'] = kompaniya
    malumot['model'] = model
    return malumot

avto0 = avto_info('gm', 'malibu', rang= 'qora', yil=2020)
print(avto0)

