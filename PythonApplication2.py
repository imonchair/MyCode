print ("Hello! Please enter your name.")
name = input()
print ('Hello ' + name + '!')
print (name + ", please specify a number, an integer or a float will work but no\nstrings!")
number1 = input()
print (name + ", You have selected: " + number1)
print (name + ", please specify a second number, remember an integer or \na float will work but no strings!")
number2 = input()
print (name + ", You have selected: " + number2)
print ("Just a recap your first number was: " + number1 + "\nand your second number was: " + number2)
print ("Are those correct? If yes please enter 'y' if incorrect please enter 'n'")
if input() == "y":
        print("Cool, just so you know their is no way that could of been wrong!")
        if number1 > number2:
            print (number1 + " is greater than " + number2)
            print ("Thank's for trying my code, " + name + "!")
        elif number1 < number2:
            print (number1 + " is less than " + number2)
            print ("Thank's for trying my code, " + name + "!")
        elif number1 == number2:
                print (number1 + " is equal to " + number2)
                print ("Thank's for trying my code, " + name + "!")
elif input() == "n":
        print("Ok let's start again!")
else:
    print("Sorry I'm not quite sure what went wrong there please try again! Remember I only recognise a lowercase 'y' for yes and a lowercase 'n' for no")
