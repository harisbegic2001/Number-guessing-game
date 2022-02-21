                        #DAY 12
import random as r


def logic(zivoti):
        while zivoti > 0:
            print(f"You have {zivoti} lives")
            answer = int(input("Enter your answer: "))

            if answer == correct_answer:
                print("YOU WON!")
                break
            
            elif answer < correct_answer:
                print("Too low")
                zivoti -= 1
                if zivoti > 0:
                    print("Guess Again")
                else:
                    print("You lost :(")

            elif answer > correct_answer:
                print("Too high")
                zivoti -= 1
                if zivoti > 0:
                    print("Guess Again")
                else:
                    print("You lost :(")
            


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

correct_answer = r.randint(1,100)

difficulty = input("Choose difficulty \"easy\" or \"hard\": ").lower()

if difficulty == "easy":
    logic(10)

elif difficulty == "hard":
    logic(5)