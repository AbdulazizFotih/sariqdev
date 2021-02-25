# def toliq_ism_yasa(ism, familiya):
#     """toliq ism qaytaruvchi funksiya"""
#     toliq_ism = f'{ism} {familiya}'
#     return toliq_ism

# talaba0 = toliq_ism_yasa('azizbek', 'tursunov')
# talaba1 = toliq_ism_yasa('azamat', 'hakimov')

# print(f'dasga kelmaga oquvchilar {talaba0} va {talaba1}')

##############

# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """To'liq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f'{ism} {otasining_ismi} {familiya}'
#     else:
#         toliq_ism = f'{ism} {familiya}'
#     return toliq_ism.title()

# talaba0 = toliq_ism_yasa('azizbek', 'tursunov' 'rahmatullayevich')
# talaba1 = toliq_ism_yasa('azamat', 'hakimov')


# print(f'dasrga kelgan oquvchlar {talaba0} va {talaba1}')


############


# def avto_info(kompaniya, model, rang, korobka, yil, narxi=None):
#     avto = {
#         'kompaniya': kompaniya,
#         'model': model,
#         'rang': rang,
#         'korobka': korobka,
#         'yil': yil,
#         'narxi': narxi
#     }
#     return avto

###############

def oraliq(min, max):
    """berilgan sonlar orasidagi
    sonni yozuvchi funksiya"""
    sonlar = []
    while min<max:
        sonlar.append(min)
        min += 1
    return sonlar

print(oraliq(0, 10))
