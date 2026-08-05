PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р
'''

RESULT = {
    words.split()[0]: int(words.split()[1][:-1])
    for words in PRICE_LIST.splitlines()
}

print(RESULT)
