#CS 30
#Owen Hipfner
#Starting Date 16 dec 2021
import list as lis


####Beta####
#Making website an object and giving it attributes that can be called on.
class Website():
    def __init__(
        self,
        name,
        description,
        url,
    ):
        self.name = name
        self.description = description
        self.url = url


#Calling a name and making it an object with attributes, the name of the object, description of it, and the url.
Wikipedia = Website("Wikipedia", "A site for information",
                    "https://en.wikipedia.org/wiki/Main_Page")
#Calling multiple names and making multiple objects with attributes.
Google = Website("Google", "A competing web browser", "https://www.google.ca/")

Youtube = Website("Youtube", "Internet video site to entertain",
                  "https://www.youtube.com/")

Twitch = Website("Twitch", "Live stream platform", "https://www.twitch.tv/")

Amazon = Website("Amazon", "Shopping site for all needs",
                 "https://www.amazon.ca/")

Netflix = Website("Netflix", "Movie and tv streaming service",
                  "https://www.netflix.com/ca/")

Disney = Website("Disney", "Has streaming app, parks to travel and movies",
                 "https://www.disney.com/")

Best_Buy = Website("Best Buy", "Electronic and tech store",
                   "https://www.bestbuy.ca/en-ca")

Bing = Website("Bing", "A competing web browser", "https://www.bing.com/")

Yahoo = Website("Yahoo", "A competing web browser", "https://ca.yahoo.com/")

#A is a variable for the while loop.
a = 1
#A while loop to keep the websites avalible.
while a == 1:
    #Importing the title from a different file.
    lis.title()
    #Input from the user so then it can.
    user_input = str(input("Search a website: "))
    print("\n")
    #If the user searches the name it will print the attributes.
    if user_input == "wikipedia":
        print(Wikipedia.name)
        print(Wikipedia.description)
        print(Wikipedia.url)
        print("\n")
    #Another possible object to search.
    elif user_input == "google":
        print(Google.name)
        print(Google.description)
        print(Google.url)
        print("\n")
    elif user_input == "youtube":
        print(Youtube.name)
        print(Youtube.description)
        print(Youtube.url)
        print("\n")
    elif user_input == "twitch":
        print(Twitch.name)
        print(Twitch.description)
        print(Twitch.url)
        print("\n")
    elif user_input == "amazon":
        print(Amazon.name)
        print(Amazon.description)
        print(Amazon.url)
        print("\n")
    elif user_input == "netflix":
        print(Netflix.name)
        print(Netflix.description)
        print(Netflix.url)
        print("\n")
    elif user_input == "disney":
        print(Disney.name)
        print(Disney.description)
        print(Disney.url)
        print("\n")
    elif user_input == "best buy":
        print(Best_Buy.name)
        print(Best_Buy.description)
        print(Best_Buy.url)
        print("\n")
    elif user_input == "bing":
        print(Bing.name)
        print(Bing.description)
        print(Bing.url)
        print("\n")
    elif user_input == "yahoo":
        print(Yahoo.name)
        print(Yahoo.description)
        print(Yahoo.url)
        print("\n")
    #The user can access the list of websites
    elif user_input == "list":
        lis.list()
    #If the user wants they can
    elif user_input == "title":
        lis.title()
    #Quit option to leave the browser
    elif user_input == "quit":
        print("Thank you for using the browser")
        a = 2
    #Any errore the user makes will print a message to help
    else:
        print('''
USE LOWER CASE AND PROPER SPELLING. 
IF ALL IS CORRECT WEBSITE IS NOT AVALIBLE''')
        print("\n")
