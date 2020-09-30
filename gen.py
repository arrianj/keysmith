import itertools
import pyinputplus as pyip
import sys
import functions
from itertools import chain
from functions import *

# begin script
startup = pyip.inputYesNo(prompt=('[?] Begin new password gen? [Y/N]: '))
if startup == 'yes':
	first_name = pyip.inputCustom(text_alert, prompt='[*] First Name: ')
	last_name = pyip.inputCustom(text_alert, prompt='[*] Last Name: ')
	use_bday = pyip.inputYesNo(prompt='[?] Include birthday? [Y/N]: ')
	if use_bday == 'yes':
		birthday = str(pyip.inputDate(prompt='[*] Enter birthday [format: MM/DD/YYYY]: '))
	else:
		pass
	skip_small = pyip.inputYesNo(prompt='[?] Skip generating results with low character counts? [Y/N]: ')
	if skip_small == 'yes':
		skip_length = (pyip.inputNum(prompt='[*] Minimum amount of characters in result?: '))
	else:
		skip_length = 0
	
else:
	sys.exit()

# generate possible representations of inputs and stores them in these variables
chrs_f_name = possibles_f_name(first_name)
chrs_l_name = possibles_l_name(last_name)

# combine the storage variables into a single set
chrs = list(chain(chrs_f_name,chrs_l_name))

# set input counter to iterate once per field
input_counter = 2

# use birthday in permutations
if use_bday == 'yes':
	chrs_bday = possibles_bday(birthday)
	input_counter += 1
	chrs = set(chain(chrs,chrs_bday))

# see what representations will be permutated
print(chrs)

# create a text file to store all the permutations
file_name = input('Insert a name for your wordlist file: ')+'.txt'
output = open(file_name, 'w')

# fill text file with results, by iterating every representation through the rest of the list, once per input field, and saving
for i in itertools.permutations(chrs,input_counter):
	temp = ''.join(i)
	if len(temp) < skip_length:
		pass
	else:
		output.write(temp + '\n')	
output.close()
