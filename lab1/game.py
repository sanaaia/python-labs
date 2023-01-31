import random

game_state = True


def check_input(input):
    if input.isdigit():
        if int(input) >= 1 and int(input) <= 100:
            return True
        else:
            print('Please enter an integer between 1 and 100!')
        return False
    else:
        print('Please enter an integer between 1 and 100!')
        return False


while game_state:
    print('Game Time!\nGuess a number between 1 and 100. You have 7 chances.')

    guesses = 7
    user_guesses = 0
    number = random.randint(1, 100)
    right_guess = False

    while user_guesses < guesses:
        user_number = input('Enter your number: ')
        if check_input(user_number):
            user_number = int(user_number)
            if user_number == number:
                print('You Win!!!')
                right_guess = True
                break
            elif user_number > number:
                print('Your guess is greater than answer')
            elif user_number < number:
                print('Your guess is lesser than answer')
            else:
                print('Please enter an integer between 1 and 100!')
            user_guesses += 1
            guesses_left = guesses - user_guesses
            print('You have', guesses_left, 'guesses left')
    if not right_guess:
        print('You Lose!!!')
        print('A guessed number is ', number)
    message = input('Do you want to play another round? Enter [n] to exit. ')
    if message == 'n':
        game_state = False
