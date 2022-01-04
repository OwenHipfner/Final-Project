#CS 30
#Owen Hipfner
#Starting Date 16 dec 2021

####Alpha####
#Giving a website a set of atributes to then print later
wikipedia_name = "Wikipeida"
wikipedia_def = "A useful tool to find information"
wikipedia_url = "https://en.wikipedia.org/wiki/Main_Page"
#Using multiple websites with atributes
google_name = "Google"
google_def = "Competing web browser"
google_url = "https://www.google.ca/"
#A is used to end the while loop
a = 1
#A while loop to keep the websites avalible
while a == 1:
    #Input from the user so then it can
    user_input = str(input("Choose a website: "))
    #If the user searches this website it will print the attributes
    if user_input == "wikipedia":
        print(wikipedia_name)
        print(wikipedia_def)
        print(wikipedia_url)
        print("\n")
    #Another possible website to search
    elif user_input == "google":
        print(google_name)
        print(google_def)
        print(google_url)
        print("\n")
    #Quit option to leave the browser
    elif user_input == "quit":
        print("Thank you for using the browser")
        a = 2
    #Any errore the user makes will print a message to help
    else:
        print('''
Use lower case and proper spelling or
That website is curently not avalible''')
        print("\n")
