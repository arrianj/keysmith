import itertools
import pyinputplus as pyip
import sys
import methods
from itertools import chain
from methods import *

# input validator function
def text_alert(text):
	if text.isalpha():
		pass
	else:
		raise Exception('Input can only contain letters.')

# begin script
startup = pyip.inputYesNo(prompt=('[?] Begin new password gen? [Y/N]: '))
if startup == 'yes':
	first_name = pyip.inputCustom(text_alert, prompt='[*] First Name: ')
	last_name = pyip.inputCustom(text_alert, prompt='[*] Last Name: ')
	use_numbers = pyip.inputYesNo(prompt='[?] Include numbers? [Y/N]: ')
	if use_numbers == 'yes':
		digit_counter = pyip.inputNum(prompt='[?] What is the highest number you want to use? [e.g. 100 would mean all numbers from 0-100]: ')
	else:
		pass
	# birthday = pyip.inputDate(prompt='[*] Enter birthday [format: MM/DD/YYYY]: ')
else:
	sys.exit()

# generate possible representations of inputs and stores them in these variables
chrs_f_name = possibles_f_name(first_name)
chrs_l_name = possibles_l_name(last_name)

# combine the storage variables into a single set
chrs = list(chain(chrs_f_name,chrs_l_name))

# set input counter to iterate once per field
input_counter = 2

# use numbers in permutations
if use_numbers == 'yes':
	input_counter += 1
	numbers = [str(i) for i in range(digit_counter+1)]

# see what representations will be permutated
print(chrs)

# create a text file to store all the permutations
file_name = input('Insert a name for your wordlist file: ')+'.txt'
output = open(file_name, 'w')

# fill text file with results, by iterating every representation through the rest of the list, once per field of input, and saving   

if use_numbers == 'no':
	for i in itertools.permutations(chrs,input_counter):
		temp = ''.join(i)
		# discard results that only contain numbers
		if temp.isnumeric():
			pass
		else:
			output.write(temp + '\n')
			
# error here is that i only want it to create a permutation that has a number
elif use_numbers == 'yes':
	for x in numbers:
		chrs = set(chain(chrs,x))
		for i in itertools.permutations(chrs,input_counter):
			temp = ''.join(i)
			# discard results that only contain numbers
			if temp.isnumeric():
				pass
			elif has_num(temp) == False:
				pass
			else:
				output.write(temp + '\n')
output.close()
