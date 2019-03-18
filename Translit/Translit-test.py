from transliterate import detect_language

string = 'Y_!в'
for i in string:
    # нельзя определить язык лишь по одному символу по этому i+i
    if detect_language(i+i) == 'ru':
        print('ru')
    else:
        print('en')
