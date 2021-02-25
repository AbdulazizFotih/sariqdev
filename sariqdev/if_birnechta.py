# yosh = int(input("yoshingizni kiritng: "))
# if yosh<=4:
# 	narx = 0
# elif yosh<=12:
# 	narx = 5000
# else:
# 	narx = 10000

# print(f'Sizga kirish {narx} so\'m')

################################


# kun = input("bugun qaysi kun? >>> ")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
# 	print("bugun dam olish kuni ;) ")
# else:
# 	print('bugun ish kuni :( ')


################################


kun = input("bugun nima kun? >>> ")
harorat = float(input('havo harorati qanday? >> '))
if kun.lower()=='yakshanba' and harorat >=30:
	print('cho\'milgani kettik')
elif kun.lower()=='yakshanba' and harorat<30:
	print('uyda qolamiz')
else:
	print('ishlashni davom ettiring ')