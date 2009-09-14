#!/usr/bin/python
# -*- coding: utf-8 -*-

#Marco Garcês - marco at garces.cc

import twitter,settings

api = twitter.Api(username=settings.TWITTER_USER,password=settings.TWITTER_PASSWD)

def del_twitter_dm(dm_id):
	api.DestroyDirectMessage(id=dm_id)
	
def get_twitter_dm():
	#api = twitter.Api(username=settings.TWITTER_USER,password=settings.TWITTER_PASSWD)
	dm_messages = api.GetDirectMessages()
	dm_input = dm_messages[0].text #string to use in get_meal()
	
 	dm_id = dm_messages[0].id #id number to delete DM after reply
	dm_user = dm_messages[0].sender_screen_name #twitter user to reply answer
	
	del_twitter_dm(dm_id)
	return dm_input #to be used in get_meal and open_menu