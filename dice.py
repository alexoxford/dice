import random
import math
import os

quit = False
valid = [1, 2, 3]
while(not quit):
	opt = ''
	while(opt == ''):
		_=os.system('cls')
		print('1 - Dice')
		print('2 - Range')
		print('3 - Quit')
		opt = input('>')
		try:
			opt = int(opt)
			if(opt not in valid):
				opt = ''
		except(ValueError):
			opt = ''
	_=os.system('cls')
	if(opt == 1):
		d = input('Enter dice in the form xdy\u00b1z: ')
		l1 = d.split('d')
		num = int(l1[0])
		l2 = []
		if('+' in l1[1]):
			l2 = l1[1].split('+')
			mod = int(l2[1])
		elif('-' in l1[1]):
			l2 = l1[1].split('-')
			mod = (-1) * int(l2[1])
		else:
			mod = 0
			l2.append(l1[1])
		die = int(l2[0])
		rep = True
		while(rep):
			if(num != 1):
				val = 0
				rolls = []
				for i in range(num):
					add = random.randint(1, die)
					rolls.append(add)
					val += add
					print(' + ' + str(add), end='') if (i != 0) else print(str(add), end='')
				val += mod
				if(mod == 0):
					print(' = ' + str(val))
				elif(mod > 0):
					print(' + ' + str(mod) + ' = ' + str(val))
				else:
					 print(' - ' + str(-mod) + ' = ' + str(val))
			else:
				val = random.randint(1, die)
				if (mod != 0):
					print(str(val) + ' + ' + str(mod) + ' = ' + str(val + mod))
				else:
					print(str(val))

			rep = False if(input('Repeat? (y/n): ') == 'n') else True
	elif(opt == 2):
		r = input('Enter range in the form xx-yy: ')
		limits = r.split('-')
		rep = True
		while(rep):
			val = random.randint(int(limits[0]), int(limits[1]))
			print(val)
			rep = False if(input('Repeat? (y/n): ') == 'n') else True
	elif(opt == 3):
		quit = True