""""
Homework 2 (task 2)

Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
Использовалось 2 функции replace с целью убрать как точки так и запятые
"""
max_len = 0
max_word = ''
base_string = (input("Введите строку: ")).replace(',', '').replace('.', '').split(' ')
for word in base_string:
    if len(word) > max_len:
        max_len = len(word)
        max_word = word
print('Самое длинное слово "', max_word, '" его длина -', max_len, 'символов')
