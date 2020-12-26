#import modules
import random

print("Welcome to Bulls and Cows \nPress any key to begin")
input("")

#define variables
usernumber = 0
userguesses = 0

#create random number
number = random.randint(1000,9999)
print("The number is {0} for debugging".format(number))

#function where user input is processed
def checknumber(userinput):
    digits = [int(x) for x in str(number)]
    digits2 = [int(x) for x in str(userinput)]
    Bulls = 0
    Cows = 0

    for i in digits:
        for ii in digits2:
            if i == ii:
                if digits.index(i) == digits2.index(ii):
                    Bulls += 1
                else:
                    Cows += 1
                digits2[digits2.index(ii)] = "extra"
                digits[digits.index(i)] = "extra1"
                    
    print("There is {0} bull/s found and {1} cow/s found".format(Bulls, Cows))

print("A random 4 digit number has been created, your job is to guess it")
print("If you give up type exit")

#main while loop where everything happens
while usernumber != number:
    print("Enter your number:")
    usernumber= str(input(""))
    userguesses += 1
    if usernumber == 'exit':
        break
    usernumber = int(usernumber)
    checknumber(int(usernumber))

#while loop finished
#final check
if usernumber == number:
    print("The number is {0}".format(number))
    print("Well done you have finished the game")
else:
    print("The number is {0}".format(number))
    print("Better Luck Next Time")
