mevalar = ['olma', 'anjir', 'anor', 'nok']
print(mevalar)
mevalar.append('ananas') # element qo'shish
print(mevalar)
mevalar.insert(2, 'kakos') # index orqali element qo'shish
print(mevalar)
del mevalar[3] # index orqali elementni o'chirish
print(mevalar)
mevalar.remove('anjir') # qiymat orqali o'chirish
print(mevalar)


###############################

doslar = ['murodjon', 'hamidullo', 'adash', 'saset']
print(f'{doslar.pop().title()} qulupne sotamizmi')
print(f'{doslar.pop().title()} bugun call of duty uynaymizmi')
print(f'{doslar.pop().title()} nima gap')
print(f'{doslar.pop().title()} domlani oldilariga boramizmi?')