import pandas

from appJar import gui

fooddrinkdf = pandas.read_csv("fooddrink.csv")
beveragelist = list(fooddrinkdf.Beverage)
foodlist = list(fooddrinkdf.Food)


# Function to greet user
def greet_user(greeting, sentinel, categoryq, readyq):
    canswer = ' '
    ranswer = sentinel
    print(greeting)
    while ranswer == sentinel:
        canswer = input(categoryq)
        ranswer = input(readyq)
    if canswer == "Beverage":
        Beverage("Welcome to our Beverage section! Here are your choices:", beveragelist,
                 "Which drink would you like or enter None? ")
    elif canswer == "Food":
        Food("Welcome to our Food section! Here are your choices:", foodlist,
             "Which food would you like or enter None? ")
    else:
        print('Sorry we do not carry that here. We hope you return when you need food or a drink.')


# Function to ask user to pick a Beverage
def Beverage(greeting, selection, pickq):
    print(greeting)
    for item in selection:
        print(item)
    beveragepick = input(pickq)
    if beveragepick == "None":
        print("Goodbye")
    elif beveragepick == "Water":
        closing("Water", 2, "Enjoy your Water!")
    elif beveragepick == "Coke":
        closing("Coke", 3, "Enjoy your Coke!")
    elif beveragepick == "Coffee":
        closing("Coffee", 3, "Enjoy your Coffee!")
    else:
        closing("Tea", 3, "Enjoy your Tea!")


# Function to ask user to pick Food
def Food(greeting, selection, pickq):
    print(greeting)
    for item in selection:
        print(item)
    foodpick = input(pickq)
    if foodpick == "None":
        print("Goodbye")
    elif foodpick == "Hot Dog":
        closing("Hot Dog", 7, "Enjoy your Hot Dog!")
    elif foodpick == "Sandwich":
        closing("Sandwich", 8, "Enjoy your Sandwich!")
    elif foodpick == "Cake":
        closing("Cake", 4, "Enjoy your Cake!")
    else:
        closing("Salad", 6, "Enjoy your Salad!")


# Function to give user total price of purchase
def closing(pickeditem, price, goodbye):
    print("Your cost for the", pickeditem, "is $" + str(price))
    more = input("Would you like to pick another item (y/n)?")
    if more == "y":
        greet_user("Great!", "n", "What category would you like to browse (Beverage, Food)? ",
                   "Ready to browse (y/n)? ")
    else:
        for l in goodbye:
            print(l)


"""
This is the function that determines code executed when each button is pressed

"""


def press(btn):
    if btn == "Exit":
        app.stop()
    elif btn == "Greeting":
        greet_user("Welcome to our store", "Grab N Go", "What category would you like to browse (Beverage, Food)? ",
                   "Ready to browse (y/n)? ")
    elif btn == "Beverage":
        Beverage("Welcome to our Beverage section! Here are your choices:", beveragelist,
                 "Which drink would you like or enter None? ")
    elif btn == "Food":
        Food("Welcome to our Food section! Here are your choices:", foodlist,
             "Which food would you like or enter None? ")
    else:
        print('Pick a valid option')


app = gui("Main Menu", "500x500")

app.addLabel("title", "Welcome to Grab N Go's Main Menu")
app.setLabelBg("title", "orange")

app.addImage("decor", "burger.gif")
app.setFont(18)

app.addButton("Greeting", press)
app.addButton("Beverage", press)
app.addButton("Food", press)
app.addButton("Exit", press)
app.go()  # displays the gui