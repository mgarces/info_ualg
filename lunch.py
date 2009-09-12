#!/usr/bin/python
# -*- coding: utf-8 -*-

#open txt and parse it to a list (dinner or lunch); returns the menu, clean without \n
import sys, os

def open_menu(choice):
	if choice == 'almoço':
		file = 'lunch.txt'
	elif choice == 'jantar':
		file = 'dinner.txt'
	else:
		print 'escolha não definida/encontrada\n'
		sys.exit()
	f = open(file, 'r')
	linhas = f.readlines()
	f.close()
	
	#clean lines from \n
	menu = []
	for item in linhas:
		menu.append(str(item).strip())
	return menu
	

#find and output desired menu
def get_meal(choice, date):
	menu = open_menu(choice)
	if date in menu:
		n = menu.index(date)
		if choice == 'almoço':
			menu_day = menu[n:n+6]
			menu_day.insert(0, choice)
			return '\n Menu %s %s: sopa de %s, %s, %s, %s\n Sobremesa: %s\n' \
			%(menu_day[0], menu_day[1], menu_day[2], menu_day[3], menu_day[4], menu_day[6], menu_day[5])
		else:
			menu_day = menu[n:n+5]
			menu_day.insert(0, choice)
			return '\n Menu %s %s: sopa de %s, %s, %s\n Sobremesa: %s\n' \
			%(menu_day[0], menu_day[1], menu_day[2], menu_day[3], menu_day[4], menu_day[5])
	
	else:
		return 'Menu não se encontra disponível\n para este dia \n'

def clearscreen(numlines=100):
	# Clear the console.
	# import os
	if os.name == "posix":
		# Unix/Linux/MacOS/BSD/etc
		os.system('clear')
	elif os.name in ("nt", "dos", "ce"):
		# DOS/Windows
		os.system('CLS')
	else:
		# Fallback for other operating systems.
		print '\n' * numlines



choice = raw_input("deseja saber o menu do almoço ou do jantar? \n")
date = raw_input("qual o dia do menu que quer?(de 1-09-2009 a 30-09-2009) \n")

print get_meal(choice, date)
os.system('clear')