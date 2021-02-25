talaba_0 = {
    'ism': 'azizbek',
    'familiya': 'tursunov',
    'yosh': 18,
    'fakultet': 'ingliz tili',
    'kusr': 1
}

print(talaba_0.items())

for kalit, qiymat in talaba_0.items():
    print(f'Kalit: {kalit}')
    print(f'Qiymat: {qiymat} \n')


telefonlar = {
    'anasxon': 'galaxy a51',
    'murodjon': 'galaxy a10s',
    'hamidullo': 'redmi 7',
    'mubosher': 'none',
    'men': 'none'
}

for k, q in telefonlar.items():
    print(f'{k.title()}ning telefoni {q}')

###

mahsulotlar = { # Do'kondagi mahsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }

print(mahsulotlar.keys())

print("do'kondagi mahsulotlar:")
for mahsulot in mahsulotlar.keys():
    print(mahsulot)

bozorlik = ['anor', 'uzum', 'non', 'baliq']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f'{mahsulot.title()} {mahsulotlar[mahsulot]} so\'m')

for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f'iltimos, do\'koningizga {buyum} ham olib keling')

print("Do'konimizdagi mahsulotlar:")
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())