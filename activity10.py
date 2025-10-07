from getpass import getpass
username = 'lance'
pword = 'lance123'
 
u = input("USERNAME --> ")
p = getpass("PASSWORD --> ")

if (u == username) and (p == pword) :		 	 	 	 
    print ("Acess Granted")
else: 		 	 	 	 	 	 	    	 
    print ("Acess Denied")