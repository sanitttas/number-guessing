import random
print("Hi! I am trying to figure out what I want to do!")
user_name = input("What is your name?")
if user_name.lower() == "sanita":
    print("Hello, boss!")
elif user_name.lower() == "staņislavs":
    print("Hello, ", user_name, ", I love you!")
else: print("Hello, ", user_name, "!")

print("Now, I want you to think of a number between 1 and 100.")
print("Done? I will try to guess it!")
print("Please answer all questions with yes/no.")

found = False

number_question1 = input("Is your number higher than 50? (yes/no)")

if number_question1.lower() == "yes":
    number_question2 = input("Is your number higher than 75? (yes/no)")

    while found == False:
        if number_question2.lower() == "yes":
            random_number = random.randint(76, 100)
        else: random_number = random.randint(51, 75)

        number_guess = input(f"Is your number {random_number} ?")

        if number_guess.lower() == "yes":
            print("I knew it!")
            found = True
        else:
            print("I am not good at this.") 
        

elif number_question1.lower() == "no":
    number_question2 = input("Is your number higher than 25? (yes/no)")

    while found == False:
        if number_question2.lower() == "yes":
            random_number = random.randint(26, 50)
        else: random_number = random.randint(1, 25)

        number_guess = input(f"Is your number {random_number} ?")

        if number_guess.lower() == "yes":
            print("I knew it!")
            found = True
        else:
            print("I am not good at this.")