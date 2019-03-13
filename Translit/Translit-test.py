import transliterate

text = transliterate.translit("нормальненько реализовал ddsdsd свой способ транслита, русские буквы нельзя шифровать, по этому я принимаю фразу на руском програмна превращаю ее в транслит и потом шифрую, рашифровываю и из транслита обратно в русский перевожу", reversed=True)
print(text)
print(transliterate.translit(text, 'ru'))