import time_in_words
import sys
import re
from fuzzytime import FuzzyTime
from random import choice
from optparse import OptionParser




def minutes_in_words():
	"""Returns the minute in words"""
	return time_in_words.MINUTES[ftime.get_minutes()]
	
def hours_in_words():
	"""Returns the hour in words"""
	return time_in_words.HOURS[ftime.get_hours()]
	
def get_preposition():
	"""Chooses a preposition considering the fuzzyfactor"""
	fuzzyfactor = ftime.get_fuzzyfactor()
	preposition = choice(time_in_words.PREPOSITIONS[fuzzyfactor])
	if fuzzyfactor == 0:
		return choice(['',preposition])
	else:
		return preposition	


def main():
	""" The main function """
	# Setting special_case variable if the time is any one of the special cases
	try:
		special_case = time_in_words.SPECIAL_CASES[ftime.to_24hour_format()]
	except KeyError:
		special_case = None
	
	# If time is any of the special case it is printed
	if special_case:
		print special_case
	else:
		# If it is exact n'o clock then on_hour_template is used
		if ftime.get_minutes() == 0 : 
			print time_in_words.on_hour_template % (get_preposition(),hours_in_words())
		else:
			print time_in_words.template % (get_preposition(),minutes_in_words(),hours_in_words())
				

# Parsing the arguments and creating the FuzzyTime object

parser = OptionParser()
parser.add_option("-t","--time",dest="time", type="string", default = None, help="TIME (HH:MM)")
(options, args) = parser.parse_args()
if options.time:
	if re.match('^[0-9]{1,2}:[0-9]{2}$', options.time):
		time = options.time.split(":")
		if 0 <= int(time[0]) <= 23 and 0 <= int(time[1]) <= 59:
			ftime = FuzzyTime(time[0],time[1])
		else:
			print "Time value is incorrect, should be between 00:00 and 23:59."
			sys.exit()
	else:
		print "Time format is incorrect, should be \"HH:MM\"."
		sys.exit()
else:
	ftime = FuzzyTime()  # Current System time will be used when invoked without arguments
	

if __name__ == '__main__':
	sys.exit(main())
