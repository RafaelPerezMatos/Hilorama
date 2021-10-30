import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low')
        elif guess > random_number:
            print('Sorry, guess again. Too high') 
    print('Yay, congrats.You have guessed the number {random_number}correctly')          

def computer_guess(x):
    low = 1
    hihg = x
    feedback = ''
    while feedback != 'c':
        if low != hihg:
            guess = random.randint(low, hihg)
        else:
            guess = low        
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (c)??').lower()
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay¡ The computer guessed your number, {guess} ,correctcly!')

computer_guess(10)