#!/usr/bin/python

from datetime import datetime

class FuzzyTime:
	""" Generates fuzzy time from the given time or system time """
	def __init__(self,hour=None,minute=None):
		now = datetime.now()
		if hour != None:
			self.hour = int(hour)
		else:
			self.hour = now.hour
		if minute != None:
			self.minute = int(minute)
		else:
			self.minute = now.minute
		
	def get_hours(self):
		""" Return fuzzy hour as str"""
		temp = self.hour
		if self.minute > 32:
			if temp == 23:
				temp = 0
			else:
				temp += 1	
		if temp > 11:
			temp = temp - 12
		return temp	
	
	def get_minutes(self):
		""" Return fuzzy minute as int """
		temp = round(self.minute / 5.0) * 5
		if temp == 60:
			return 0
		else:
			return int(temp)
				
	
	def get_fuzzyfactor(self):
		""" Returns the fuzzy factor which helps in determining prepositions """
		fuzzyfactor = self.minute % 5
		if fuzzyfactor in [1,2]:
			return 1
		elif fuzzyfactor in [3,4]:
			return -1
		else:
			return 0		# When minute is exact multiple of 5
					
	def to_24hour_format(self):
		""" Returns time in 24 hour format """
		return "%02d:%02d" % (self.hour,self.minute)
