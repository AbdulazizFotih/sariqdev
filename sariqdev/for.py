mehmonlar = ['mubosher', 'g\'olibjon', 'murodjon', 'anasxon']
for mehmon in mehmonlar:
	print(mehmon.title())

for mehmon in mehmonlar:
	print(f'{mehmon.title()} bugun baliq yegani chiqamizmi?')

for mehmon in mehmonlar:
	print(mehmon)
print(mehmonlar)

sonlar = list(range(1, 11))
for son in sonlar:
	print(f'{son} ning kvadrati {son**2} ga teng')

numbers = list(range(1, 11))
numbers_kvadrati = []
for number in numbers:
	numbers_kvadrati.append(number**2)

print(numbers)
print(numbers_kvadrati)


# doslar = []
# print('5 ta do\'stingizni ismini kiriting:')
# for n in range(5):
# 	doslar.append(input(f'{n+1}-dostingizni kiriting:'))
# print(doslar)

