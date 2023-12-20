import _codecs
import time

print("WELCOME!!!1111!1!11!") #intro
print('To the AMAAAAAAZING PASSWORD MANAGER!!!!!!')



def add_info(a, u, p):
	in_a = _codecs.encode(a, 'rot13')
	in_u = _codecs.encode(u, 'rot13')
	in_p = _codecs.encode(p, 'rot13')
	with open('pw.txt', 'a') as f:
		f.write('\n' + str(in_a))
		f.write('\n' + str(in_u))
		f.write('\n' + str(in_p))

def find_info(hut):
	with open('pw.txt', 'r') as f:
		read = f.readlines()
	modified = []
	for lime in read:
		modified.append(lime.strip())
	in_p = _codecs.encode(hut, 'rot13')
	info = modified.index(in_p)
	print(hut)
	username = modified[int(info + 1)]
	in_p = _codecs.decode(username, 'rot13')
	print(f'Username: {in_p}')
	pwd = modified[int(info + 2)]
	in_p = _codecs.decode(pwd, 'rot13')
	print(f'Password: {in_p}')	
	read = []

def edit_info(x):
	with open('pw.txt', 'r') as f:
		read = f.readlines()
	modified = []
	for line in read:
		modified.append(line.strip())
	eq = _codecs.encode(str(x), 'rot13')
	e = modified.index(eq)
	pnew_user = _codecs.encode(modified[e + 1], 'rot13')
	pnew_pass = _codecs.encode(modified[e + 2], 'rot13')	
	print("Existing Username: " + pnew_user)
	print("Existing Password: " + pnew_pass)
	new_user = input("New Username: ")
	new_pass = input("New Password: ")
	pnew_user = _codecs.encode(new_user, 'rot13')
	pnew_pass = _codecs.encode(new_pass, 'rot13')
	modified[e + 1] = pnew_user
	modified[e + 2] = pnew_pass
	open('pw.txt', 'w').close()
	with open('pw.txt', 'a') as f:
		for x in modified:
			f.write(x + "\n")

while True:
	choice = input('Do you want to add, view or edit a password? (a/v/e/q to quit)? ').lower()
	valid_choices = ['a', 'v', 'e', 'q']

	if choice not in valid_choices:
		while choice not in valid_choices:
			print("Invalid Response. Please choose (a/v/e/q to quit)?")
			choice = input('Do you want to add, view or edit a password? (a/v/e/q to quit)? ').lower()
	
	if choice == 'q':
		break
	elif choice == 'a':
		print("Sure! Let's add a password!")
		print("Just give me the details!")
		associate = input('What are you going to use this password for? ')
		user = input("What is the username? ")
		password = input('What is the password? ')
		add_info(associate, user, password)
		print("Information has been added successfully")
		time.sleep(2)
	elif choice == 'v':
		print("Sure! Let's view an existing password!")
		find = input("What are you going to use this info for? ")
		find_info(find)
	elif choice == 'e':
		print("Sure! Let's edit an existing password!")
		e_find = input("Which password would you like to edit? ")
		edit_info(e_find)
		print("Changes have been applied successfully.")
