# Module that contains the word equivalent for hours and minutes


HOURS = ['twelve',  'one',  'two',  'three',  'four',  'five',  'six',  'seven',  'eight',  'nine',  'ten',  'eleven' ]

MINUTES = {
  5:  'five past',
  10: 'ten past',
  15: 'quarter past',
  20: 'twenty past',
  25: 'twenty-five past',
  30: 'half past',
  35: 'twenty-five to',
  40: 'twenty to',
  45: 'fifteen to',
  50: 'ten to',
  55: 'five to'
			}

PREPOSITIONS = {
  -1: ['almost', 'nearly'],
  0: ['exactly', 'precisely', 'now', ''],
  1: ['after', 'right after', 'shortly after']
				}


SPECIAL_CASES = {
  '23:58': "It's round about midnight.",
  '23:59': "It's round about midnight.",
  '00:00': "it's midnight.",
  '00:01': "It's round about midnight.",
  '00:02': "It's round about midnight.",
  '12:00': "it's noon."
}

on_hour_template = "It's %s %s o'clock." # % (preposition,hour)  used when time in exactly n' o clock
template = "It's %s %s %s"  # % (prepositon,minutes,hour)  
