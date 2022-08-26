import random
import math

print ("Welcome to Rock Paper Scissors Game by Chinazor")
print("************************************************")

def play():
    get_user_choice = input("get_user_choice 'R' for rock, 'P' for paper, 'S' for scissors\n")
    get_user_choice = get_user_choice.upper()

    get_computer_choice = random.choice(['R', 'P', 'S'])

    if get_user_choice == get_computer_choice:
        return (0, get_user_choice, get_computer_choice)

    if get_winner(get_user_choice, get_computer_choice):
        return (1, get_user_choice, get_computer_choice)

    return (-1, get_user_choice, get_computer_choice)


def get_winner(user_choice, computer_choice):
    if (user_choice == 'R' and computer_choice == 'S') or (user_choice == 'S' and computer_choice == 'P') or (user_choice == 'P' and computer_choice == 'R'):
        return True
    return False

def play_best_of(n):
    user_choice_wins = 0
    computer_choice_wins = 0
    wins_necessary = math.ceil(n/2)
    while user_choice_wins < wins_necessary and computer_choice_wins < wins_necessary:
        result, get_user_choice, get_computer_choice = play()
        
        if result == 0:
            print('It is a tie!. Your choice {} is the same as computer choice. \n'.format(get_user_choice))

        elif result == 1:
            user_choice_wins += 1
            print('You won!. Your choice is {} and the computer choice is {}. \n'.format(get_user_choice, get_computer_choice))
        else:
            computer_choice_wins += 1
            print('You lost!. Your choice is {} and the computer choice is {}. :(\n'.format(get_user_choice, get_computer_choice))
        print('\n')

    if user_choice_wins > computer_choice_wins:
        print('Incredible! You have achieved the wins necessary of {} games. :D'.format(n)) 
    else:
        print('This is sad! Try again next time. The computer achieved the wins necessary for {} games'.format(n))  

if __name__== '__main__':
    play_best_of(7)

