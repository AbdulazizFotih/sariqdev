car_0 = {'model': 'ferrari', 'rang': 'qizil'}
print(car_0['rang'])

talaba_0 = {'ism': 'azizbek tursunov', 'yosh': 19, 't_yili': 2002 }
print(talaba_0)
talaba_0['kurs'] = 4 # qiymat qo'shish
print(talaba_0)
talaba_0['fakultet'] = 'informatika'
print(talaba_0)
talaba_0['fakultet'] = 'ingliz tili'
print(talaba_0)

del talaba_0['yosh'] # yosh degan kalit so'zni o'chirish
print(talaba_0)

telefonlar = {
    'anasxon': 'galaxy a51',
    'murodjon': 'galaxy a10s',
    'hamidullo': 'redmi 7',
    'mubosher': 'none',
    'men': 'none'
}
print(telefonlar)

phone = telefonlar['murodjon']
print(f'Murodning telefoni {phone}')

phone = telefonlar.get('hazan', 'bunday ism mavjud emas')
print(phone)