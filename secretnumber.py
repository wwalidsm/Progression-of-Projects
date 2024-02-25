#lets create a game in which a secret number is entered
#and a friend has to guess it 

# correct_number = int(input(Have your friend enter a number but dont look: ))
# print(correct_number)

correct_number=int(input("Have your friend enter a number 1-10 but dont look: "))

for i in range(15):
    print("\t")

while correct_number>10 or correct_number<1:
    print("sorry thats not valid tell your friend to try again")
    correct_number=int(input("Have your friend enter a number 1-10 but dont look: "))

for i in range(15):
    print("\t")
print("this is a valid entry get ready to guess")

user_guess=int(input("Whats your guess?: "))

while user_guess!=correct_number:
    if user_guess>correct_number:
        print("close, but your friends number was lower")
        user_guess=int(input("Whats your new guess?: "))
    elif user_guess<correct_number:
        print("close, but your friends number was higher")
        user_guess=int(input("Whats your new guess?: "))

print(f"yay the number was in fact {correct_number}, thanks for playing")






