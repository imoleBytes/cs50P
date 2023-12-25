#!/usr/bin/python3

dic = {}

while True:
	try:
		user_input = input().lower()
	except:
		print()
		break
	if user_input in dic:
		dic[user_input] += 1
	else:
		dic[user_input] = 1

for i in sorted(dic):
	print(f"{dic[i]} {i.upper()}")
