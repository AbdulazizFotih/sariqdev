def bahola(ismlar):
	baholar = {}
	while ismlar:
		ism = ismlar.pop()
		baho = input(f"Talabac {ism.title()}ning bahosini kiriting: ")
		baholar[ism]=int(baho)
	return baholar

talabalar = [
	'azizbek',
	'samandar',
	'xurshida',
]

baholar = bahola(talabalar)
print(baholar)