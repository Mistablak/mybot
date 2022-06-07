import time
import webbrowser


def message_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    message_pause("Hello! I'm your friend, Amanda.\n")
    message_pause("I'm here to guide you throughout your journey\n "
                  "to becoming a web developer\n")
    message_pause("First of all, i need to find out the aspect\n "
                  "of Web development you wish to learn.\n")
    message_pause("Web-development is divided into front-end\n "
                  "and back-end development\n")
    message_pause("As found on Wikipedia, Front-end web development\n "
                  "refers to the development of the graphical \n "
                  " user interface of a website,\n "
                  "through the use of HTML, CSS, & JavaScript,\n "
                  "so that users can view and interact with that website\n")
    message_pause("While back-end web development refers to the\n "
                  "server-side of development which focuses on the\n "
                  "communications between the database and the browser.\n "
                  "including scripting and website architecture\n")
    message_pause("Meanwhile, a combination of these two componenets is\n "
                  "what we know as full-stack web development\n")
    message_pause("If you wish to learn front-end web development, then you\n "
                  "should learn HTML, CSS, JavaScript, Bootstrap, React and\n "
                  "/or other front end libraries and frameworks\n")
    message_pause("But if you wish to learn back-end development, you have\n "
                  "to learn Python, Javascript, Ruby,PHP, C#, Java and "
                  "other back-end languages\n")
    message_pause("If you aspire to be a full-stack developer,\n "
                  "you know what to do of course\n")
    message_pause("Take your time and master on both components "
                  "and their relevant languages.\n")
    what_to_learn()


def learn_front_end():
    message_pause("That\'s a great choice i must say\n")
    message_pause("So these are the languages you have to learn:\n"
                  "HTML, CSS, JavaScript\n")
    message_pause("You can learn these languages on the following platforms\n"
                  "1. Freecodecamp\n" "2. W3schools\n")
    where_to_learn()


def learn_back_end():
    message_pause("You've made a good choice\n")
    message_pause("So these are the languages you should learn: Java,\n "
                  " Python, JavaScript, PHP, and other back-end\n "
                  "frameworks & libraries\n")
    message_pause("You can learn these languages on these platforms\n "
                  "1. Freecodecamp\n "
                  "2. W3schools\n")
    where_to_learn()


def learn_full_stack():
    message_pause("That\'s great!")
    message_pause("So you will have to learn HTML, CSS,JavaScript, Java,\n"
                  "Python, PHP, and other web dev frameworks and libraries\n")
    message_pause("You can learn these languages on the following platforms\n "
                  "Freecodecamp, W3schools, Udacity, and Pluralsight\n")
    for_full_stack()


def freecodecamp():
    message_pause("redirecting you to freecodecamp in a moment")
    webbrowser.open('https://www.freecodecamp.org/learn/')


def w3schools():
    message_pause("redirecting you to W3schools")
    webbrowser.open('https://www.w3schools.com/')


def udacity():
    message_pause("redirecting you to Udacity")
    webbrowser.open('https://www.udacity.com/')


def pluralsight():
    message_pause("redirecting you to Pluralsight")
    webbrowser.open('https://www.pluralsight.com/')


def what_to_learn():
    specialization = input("What do you want to learn?\n "
                           "Front-end\n "
                           "Back-end\n "
                           "Full-stack\n "
                           "Please select one\n").lower()

    if 'front-end' in specialization:
        learn_front_end()
    elif 'back-end' in specialization:
        learn_back_end()
    elif 'full-stack' in specialization:
        learn_full_stack()
    else:
        message_pause("please enter a valid response")
        what_to_learn()


def where_to_learn():
    learn = input("where do you want to learn from?\n"
                  "1. Freecodecamp\n"
                  "2. w3schools\n")
    if learn == '1':
        freecodecamp()
    elif learn == '2':
        w3schools()
    else:
        message_pause("please enter a valid response")
        where_to_learn()


def for_full_stack():
    learn = input("where do you want to learn from?\n "
                  "1. Freecodecamp\n "
                  "2. w3schools\n "
                  "3. Udacity\n "
                  "4. Pluralsight\n ")
    if learn == '1':
        freecodecamp()
    elif learn == '2':
        w3schools()
    elif learn == '3':
        udacity()
    elif learn == '4':
        pluralsight()
    else:
        message_pause("please enter a valid response")
        for_full_stack()


def another_chance():
    another_choice = input("Would you like to make another choice?\n "
                           "Please say 'yes' or 'no'\n").lower()
    if 'yes' in another_choice:
        message_pause("Very good. I am happy to give you another chance.\n")
        what_to_learn()

    elif 'no' in another_choice:
        message_pause("okay, goodbye")
        exit()

    else:
        message_pause("please enter a valid response")
        another_chance()


def talk_to_amanda():
    intro()
    what_to_learn()
    another_chance()


talk_to_amanda()
