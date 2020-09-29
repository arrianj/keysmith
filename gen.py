import itertools
import pyinputplus as pyip
import sys
from itertools import chain
from inputbreakdown import *

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
	use_numbers = pyip.inputYesNo(prompt='[?] Should I include numbers? [Y/N]: ')
	# digit_counter = pyip.inputNum(max=3, prompt='[?] Up to how many digits should I generate? [4 => 0-9999]: ')
	# birthday = pyip.inputDate(prompt='[*] Enter birthday [format: MM/DD/YYYY]: ')
else:
	sys.exit()

# generate possible representations of inputs and stores them in these variables
chrs_f_name = possibles_f_name(first_name)
chrs_l_name = possibles_l_name(last_name)
numbers = ['1','2','3','4','5','6','7','8','9','0']

# combine the storage variables into a single set
chrs = set(chain(chrs_f_name,chrs_l_name))

# optional inputs
if use_numbers == 'yes':
	chrs = set(chain(chrs,numbers))
else:
	pass

# see what representations will be permutated
print(chrs)

# create a text file to store all the permutations
file_name = input('Insert a name for your wordlist file: ')+'.txt'
output = open(file_name, 'w')

# fill text file with results, by iterating every representation through the rest of the list, once per representation, and saving   
for i in itertools.permutations(chrs,2):
	temp = ''.join(i)
	# if loop discards results that only contain numbers permutated onto other numbers
	if temp.isnumeric():
		pass
	else:
		output.write(temp + '\n')
output.close()