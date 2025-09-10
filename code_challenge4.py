print("Hello, welcome to manga finder")
print("Select your genre")
print("1. Horror")
print("2. Drama")
print("3. Action")
Genre = input("Pick your wanted Genre (1/2/3):")

if Genre == '1':
    print("Wow, you chose Horror, that is scary!")
    print("Choose what Decade your Manga is (1/2):")
    print("1. 2000")
    print("2. 2010")
elif Genre == '2':
    print("The Genre that you chose is Drama, whta a great choice!")
    print("Choose what Decade your Manga is (1/2):")
    print("1. 2000")
    print("2. 2010")
elif Genre == '3':
    print("The Genre that you chose is Action, that's cool!")
    print("Choose what Decade your Manga is (1/2):")
    print("1. 2000")
    print("2. 2010")

else:
    print("sorry we don't have that kind of manga")

Decade = input("Enter year range (1/2): ")

if Decade ==  '1':
    print("The Decade that you chose is 2000")
    print("Select length (1/2/3): ")
    print("1. Short")
    print("2. Medium")
    print("3. Long") 
elif Decade == '2':
    print("The Decade that you chose is 2010")
    print("Select length (1/2/3): ")
    print("1. Short")
    print("2. Medium")
    print("3. Long") 

else:
    print("sorry we don't have that kind of mangga")

length = input("choose how long your manga is (1/2/3): ")

if length == '1':
    print("Your chosen length is Short")
elif length == '2':
    print("Your chosen length is Medium")
elif length == '3':
    print("Your chosen length is Long")

if Genre == '1'and Decade == '1' and length == '1':
    print("here are the manga that you might be looking for:")
    print("Kenji Oiwa")
elif Genre == '2'and Decade == '1' and length == '1':
    print("here are the manga that you might be looking for:")
    print("The Gods Lie")
elif Genre == '3'and Decade == '1' and length == '1':
    print("here are the manga that you might be looking for:")
    print("All You Need is Kill")
elif Genre == '1'and Decade == '2' and length == '1':
    print("here are the manga that you might be looking for:")
    print("Prasyte")
elif Genre == '2'and Decade == '2' and length == '1':
    print("here are the manga that you might be looking for:")
    print("One Shot")
elif Genre == '3'and Decade == '2' and length == '1':
    print("here are the manga that you might be looking for:")
    print("Puella Magi")
    
else:
    print("sorry we don't have that kind of manga")
