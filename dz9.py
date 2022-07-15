#!/usr/bin/python3

# Регулярные выражения

# 1. Извлеките никнейм пользователя, имя домена и суффикс из данных email адресов.
# emails = "zuck26@facebook.com page33@google.com jeff42@amazon.com"
# # требуеый вывод
# [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]

import re

emails = "zuck26@facebook.com page33@google.com jeff42@amazon.com"
regexp = "(\w+)[@]{1}(\w+)[\.]{1}(\w+)"
res = re.findall(regexp,emails)
print(res)

# 2. Извлеките все слова, начинающиеся с ‘b’ или ‘B’ из данного текста.
# text = """Betty bought a bit of butter, But the butter was so bitter, So she bought some
# better butter, To make the bitter butter better."""
# # требуеый вывод
# ['Betty', 'bought', 'bit', 'butter', 'But', 'butter', 'bitter', 'bought', 'better', 'butter', 'bitter',
# 'butter', 'better']

text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some \
better butter, To make the bitter butter better."

regexp = '[bB][a-zA-Z]+'
res = re.findall(regexp,text)
print(res)

# 3. Уберите все символы пунктуации из предложения
# sentence = """A, very very; irregular_sentence"""
# # требуеый вывод
# A very very irregular sentence

sentence = "A, very very; irregular_sentence"
regexp = '[,\.;_\s]+'
res = re.sub(regexp,' ',sentence)
print(res)

# 4. Очистите следующий твит, чтобы он содержал только одно сообщение
# пользователя. То есть, удалите все URL, хэштеги, упоминания, пунктуацию, RT и CC.
# tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to
# code today https://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
# # требуеый вывод
# 'Good advice What I would do differently if I was learning to code today'

tweet = 'Good advice! RT @TheNextWeb: What I would do differently if I was learning to \
        code today https://t.co/lbwej0pxOd cc: @garybernhardt #rstats'
tweet = re.sub('RT|cc', '', tweet)
tweet = re.sub('[@#]\S+', '', tweet)
tweet = re.sub('http\S+\s*', '', tweet)
tweet = re.sub('[,!:\.;_\s]+', ' ', tweet)
print(tweet)