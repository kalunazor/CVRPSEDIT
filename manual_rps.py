import random

def play():
    get_user_choice = input("get_user_choice 'R' for rock, 'P' for paper, 'S' for scissors\n")
    get_user_choice = get_user_choice.upper()

    get_computer_choice = random.choice(['R', 'P', 'S'])

    if get_user_choice == get_computer_choice:
        return "There's a tie!. Your choice and the computer choice is {}.".format(get_computer_choice)

    if get_winner(get_user_choice, get_computer_choice):
        return "You won!. Your choice is {} and the computer choice is {}.".format(get_user_choice, get_computer_choice)

    return "You lost!. Your choice is {} and the computer choice is {}. :(".format(get_user_choice, get_computer_choice)



def get_winner(user_choice, computer_choice):
    if (user_choice == 'R' and computer_choice == 'S') or (user_choice == 'S' and computer_choice == 'P') or (user_choice == 'P' and computer_choice == 'R'):
        return True
    return False

if __name__== '__main__':
    print(play())

