#!/usr/bin/python
# -*- coding: utf-8 -*-

#Marco Garcês - marco at garces.cc

import twitter,settings,sys

api = twitter.Api(username=settings.TWITTER_USER,password=settings.TWITTER_PASSWD)

def del_twitter_dm(dm_id):
	for id in dm_id:
		api.DestroyDirectMessage(id)
	
def get_twitter_dm():
	dm_messages = api.GetDirectMessages()
	if dm_messages == []:
		print "no new DM messages"
		sys.exit()
		
	else:
			
			dm_input = dm_messages[0].text #string to use in get_meal()
	
 			dm_id = dm_messages[0].id #id number to delete DM after reply
			dm_user = dm_messages[0].sender_screen_name #twitter user to reply answer
	
			dm_return = [dm_user,dm_input,dm_id] 
		
		
			#return dm_input #to be used in get_meal and open_menu
			return dm_return
		
def send_twitter_dm(user, output):
	api = twitter.Api(username=settings.TWITTER_USER,password=settings.TWITTER_PASSWD)

	if api.PostDirectMessage(user,output):
		return 1
	else:
		return 0
	