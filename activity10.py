from getpass import getpass

username = 'lance'
pword = 'lance123'

u = input("USERNAME --> ")
p = input("PASSWORD --> ")


if (u == username) and (p == pword) :
	print("Access Granted")
else:
	print("Access Denied")