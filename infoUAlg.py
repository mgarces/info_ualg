#!/usr/bin/python
# -*- coding: utf-8 -*-

#Marco Garcês - marco at garces.cc
 
import sys,os,twitter,settings
#twitter api provided by http://code.google.com/p/python-twitter/

#open txt and parse it to a list (dinner or lunch); returns the menu, clean without \n
def open_menu(choice):
	if choice == 'almoço':
		file = settings.LUNCH_FILE
		f = open(file, 'r')
		linhas = f.readlines()
		f.close()
		#clean lines from \n
		menu = []
		for item in linhas:
			menu.append(str(item).strip())
		return menu
	elif choice == 'jantar':
		file = settings.DINNER_FILE
		f = open(file, 'r')
		linhas = f.readlines()
		f.close()
		#clean lines from \n
		menu = []
		for item in linhas:
			menu.append(str(item).strip())
		return menu
	else:
		menu = []
		return menu
 
#find and output desired menu
def get_meal(choice, date):
	menu = open_menu(choice)
	if menu == []:
		return 'escolha não definida/encontrada\n'
	elif date in menu:
		n = menu.index(date)
		if choice == 'almoço':
			menu_day = menu[n:n+6]
			menu_day.insert(0, choice)
			
			return 'Menu %s %s: sopa de %s, %s, %s, %s. Sobremesa: %s' \
			%(menu_day[0], menu_day[1], menu_day[2], menu_day[3], menu_day[4], menu_day[6], menu_day[5])
			
		else:
			menu_day = menu[n:n+5]
			menu_day.insert(0, choice)
			
			return 'Menu %s %s: sopa de %s, %s, %s. Sobremesa: %s' \
			%(menu_day[0], menu_day[1], menu_day[2], menu_day[3], menu_day[4], menu_day[5])
			
			
	else:
		return 'Menu não se encontra disponível\n para este dia \n'
 	
#this creates the api object, and the dm_messages list
api = twitter.Api(username=settings.TWITTER_USER,password=settings.TWITTER_PASSWD)
dm_messages = api.GetDirectMessages()

for t in dm_messages:
	user = t.sender_screen_name
	user_input = t.text.split()
	
	service = user_input[0].encode("utf-8")
	choice = user_input[1].encode("utf-8")
	date = user_input[2].encode("utf-8")
	
	output = get_meal(choice, date).decode("utf-8")
	
	dm_id = t.id
	
	api.PostDirectMessage(user,output)
	api.DestroyDirectMessage(dm_id)