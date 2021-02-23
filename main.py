import random

result_list = []


class NegativeNumberError(Exception):
    def __str__(self):
        return "The number can't be negative!"


class MoreThenMlnError(Exception):
    def __str__(self):
        return "Invalid input! The number can't be bigger than 1000000."


def random_num():
    return random.randint(0, 1_000_000)


def result():
    print("\nYou won: {},".format(result_list.count(1)))
    print("The robot won: {},".format(result_list.count(0)))
    print("Draws: {}".format(result_list.count(3)))


def check_num(number):
    rnd_num = random_num()
    robot_num = random_num()
    r1 = abs(rnd_num - robot_num)
    r2 = abs(rnd_num - number)
    print(f"\nThe robot entered the number {robot_num}.")
    print(f"The goal number is {rnd_num}.")
    if r1 < r2:
        print("The robot won!\n")
        result_list.append(0)
    elif r1 > r2:
        print("You won!\n")
        result_list.append(1)
    else:
        print("Draw\n")
        result_list.append(3)


def number_game():
    while True:
        user_num = input("\nWhat is your number?\n")
        if user_num == "exit game":
            result()
            break
        try:
            user_num = int(user_num)
            if user_num < 0:
                raise NegativeNumberError
            elif user_num > 1_000_000:
                raise MoreThenMlnError
            else:
                check_num(int(user_num))
        except ValueError:
            print("A string is not a valid input!")
        except NegativeNumberError as nne:
            print(nne)
        except MoreThenMlnError as mtme:
            print(mtme)


def rpc_game():
    options = {"rock": "paper",
               "paper": "scissors",
               "scissors": "rock"}
    while True:
        user_choice = input("\nWhat is your move?\n").lower()
        robot_choice = random.choice(list(options.keys()))
        if user_choice == "exit game":
            result()
            break
        if user_choice not in options:
            print("No such option! Try again!")
        elif user_choice == robot_choice:
            print("The robot chose paper")
            print("It's a draw!")
            result_list.append(3)
        elif user_choice != options[robot_choice]:
            print(f"The robot chose {robot_choice}")
            print("The robot won!")
            result_list.append(0)
        elif user_choice == options[robot_choice]:
            print(f"The robot chose {robot_choice}")
            print("You won!")
            result_list.append(1)


def main():
    while True:
        user_game = input("Which game would you like to play?\n")
        if user_game == "Rock-paper-scissors":
            rpc_game()
            break
        elif user_game == "Numbers":
            number_game()
            break
        else:
            print("\nPlease choose a valid option: Numbers or Rock-paper-scissors?\n")


main()
