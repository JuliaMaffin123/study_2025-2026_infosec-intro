#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import string

# Генерирует случайный ключ такой же длины, как и текст. Состоит из случайных букв и цифр
def generate_key_hex(text):
	key = ''
	for i in range(len(text)): # Проходим по каждому символу исходного ттекста
		key += random.choice(string.ascii_letters + string.digits)
	return key

# Шифрование и дешифрование методом XOR
# Возвращает результат XOR между каждым символом text и соответствующим символом key
def en_and_de_cript(text, key):
	res = ''
	for i in range(len(text)): # Проходим по каждому символу исходного ттекста
		# ord(text[i]) - числовой код символа
		# i % len(key) - чтобы если текст длиннее ключа, то все повторялось циклически
		# chr() - превращает числовой код обратно в символ
		res += chr(ord(text[i]) ^ ord(key[i % len(key)]))
	return res

# Находит возможные ключи, которые превращают часть шифротекста
def find_possible_keys(text, fragment):
	possible_keys = []
	for i in range(len(text)-len(fragment)+1): # чтобы не выйти за границы строки
		poss_key = ''
		for j in range(len(fragment)): # Для каждой позиции i проходим по всем символам fragment
			poss_key += chr(ord(text[i+j]) ^ ord(fragment[j]))
		possible_keys.append(poss_key)
	return possible_keys

print("\nЗадание 1")
open_text = "С Новым Годом, друзья!"
key = generate_key_hex(open_text)
ciphertext = en_and_de_cript(open_text, key)
print("Открытый текст:", open_text)
print("Ключ:", key)
print("Зашифрованный текст:", ciphertext)

print("\nЗадание 2")
found_keys = find_possible_keys(ciphertext, open_text)
print("Найденные возможные ключи (первые 5):", found_keys[:5])
print("Проверка первого ключа:")
decripted = en_and_de_cript(ciphertext, found_keys[0])
print("Расшифровка:", decripted)
print("Совпадает с исходным:", decripted == open_text)
