import random

def get_number():
    while True:
        try:
            number=int(input("enter your number:"))
            return number
        except ValueError:
            print("please enter a number")


def get_random_number():
    number = random.randint(1, 100)
    tries=0
    while True:
        guess=get_number()
        tries+=1
        if guess>number:
            print("Too high!")
        elif guess<number:
            print("Too low!")
        else:
            print(f"You got it in {tries} tries")
            break
get_random_number()