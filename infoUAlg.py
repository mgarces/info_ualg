#!/usr/bin/python
# -*- coding: utf-8 -*-
#Marco Garcês - marco at garces.cc
 
import sys, os, twitter, settings

#open txt and parse it to a list (dinner or lunch); returns the menu, clean without \n
def open_menu(choice):
	if choice == 'almoço':
		file = settings.LUNCH_FILE
	elif choice == 'jantar':
		file = settings.DINNER_FILE
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

# def get_twiiter_dm()

#user input is the string the user enters 
user_input = raw_input().split()
#at the moment this is not implemented, ignore for now
service = user_input[0]
#at this moment, "choice" is what type of menu the user wants (jantar ou almoço)
choice = user_input[1]
#date is self explanatory
date = user_input[2]

print get_meal(choice, date)