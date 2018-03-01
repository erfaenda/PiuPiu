bri = set(['Бразилия', 'Россия', 'Индия'])
'Индия' in bri

'США' in bri
print(bri)
bric = bri.copy()
bric.add('Китай')
bric.issuperset(bri)
bri.remove('Россия')
bri & bric # OR bri.intersection(bric)
print(bri)
print(bric)