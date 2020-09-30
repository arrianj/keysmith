def text_alert(text):
	if text.isalpha():
		pass
	else:
		raise Exception('Input can only contain letters.')

def possibles_f_name(fname):
    # iterates first name input through a variety of possible representations, saves values to a set
    f_name_vals = []
    f_name_vals.append(fname.upper())
    f_name_vals.append(fname.lower())
    f_name_vals.append(fname.capitalize())
    f_name_vals.append(fname.upper()[::-1])
    f_name_vals.append(fname.lower()[::-1])
    f_name_vals.append(fname.capitalize()[::-1])
    f_name_vals.append(fname.upper()[0])
    f_name_vals.append(fname.upper()[0]+'.')
    f_name_vals.append(fname.lower()[0])
    f_name_vals.append(fname.lower()[0]+'.')
    return f_name_vals

def possibles_l_name(lname):
    # iterates last name input through a variety of possible representations, saves values to a set
    l_name_vals = []
    l_name_vals.append(lname.upper())
    l_name_vals.append(lname.lower())
    l_name_vals.append(lname.capitalize())
    l_name_vals.append(lname.upper()[::-1])
    l_name_vals.append(lname.lower()[::-1])
    l_name_vals.append(lname.capitalize()[::-1])
    l_name_vals.append(lname.upper()[0])
    l_name_vals.append(lname.upper()[0]+'.')
    l_name_vals.append(lname.lower()[0])
    l_name_vals.append(lname.lower()[0]+'.')
    return l_name_vals

def possibles_bday(bday):
    # creates possible string represtations of values in submitted birth date, and accounts for birth dates and months starting with 0
    bday_vals = []
    bday_vals.append(bday[0:4])
    bday_vals.append(bday[2:4])
    bday_vals.append(bday[5:7])
    bday_vals.append(bday[8:10])
    if bday[5] == '0':
        bday_vals.append(bday[6:7])
    if bday[8] == '0':
        bday_vals.append(bday[9:10])

    return bday_vals