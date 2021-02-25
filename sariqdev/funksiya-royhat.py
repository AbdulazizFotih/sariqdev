def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f'Talaba {ism.title()}ning bahosini kiritng: ')
        baholar[ism]=baho
    return baholar

talabalar = ['azizbek', 'murodjon', 'anasxon', 'mubosher']
baholar = bahola(talabalar[:])
print(baholar)
print(talabalar)