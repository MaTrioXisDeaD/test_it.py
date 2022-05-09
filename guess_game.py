

import random



def warning():
    if z > 50 or z < 1:
        print("Your input doesn't match with the range of number of this game.")
    if z != int():
        print("Hey! you are suppose to type integer number.")

def to_infinity():
    index = 0
    while True:
        yield index
        index += 1

def compare(z,a):
    if z < a:
        print("Please try a larger number")
    elif z > a:
        print("Please try a smaller number")


print("Hey there! Would you like to play a new game ?")
c = input("Type yes or no: ").lower()
for i in to_infinity():
    if c == "yes":
        print('''Okey then user! 
This is a new game "Guess the number" 
The certain rules of this game are:
    1. There is a secret number between 1-50, which you have to guess.
    2. you will be given 7 chance to guess the number.
    3. After each of your attempt you will be given the hint weather your inputted number is larger or smaller than the secret number.
    4. If you print any other type of data-type other than 'integer' you will lost the game. ''')
        a = 21
        print("Let's start the game.")
        try:
            for i in range(7):
                z = input("Enter a number: ")
                z = int(z)
                if z == a :
                    print("Yah! you won the game.")
                    break
                elif z != a :
                    warning()
                    compare(z,a)
                    print("Try left:", (6 - i))
            break
        except:
            if z != int():
                    print("Hey! you are suppose to type integer number.")
            print("OOPs! You lost the game.")
        finally:
            if z != a and z == int():
                print("OOPs! You exceed your limit.")
            print("Hope to se you again.")
            break
    elif c == "no":
        print("Ok! See you next time.")
        break
    else:
        print("Keyword not detected.")
        c = input("Type yes or no: ").lower()
    if i == 3:
        continue



