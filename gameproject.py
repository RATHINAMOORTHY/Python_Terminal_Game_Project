import random
print('''#--Welcome to Karthick's terminal digit guessing game!--#
       You've to guess the correct 3 digit number combination!''')

answer = []

def find_answer(my_guess,secret_code):
    if my_guess == secret_code:
        return 'WINNER'

    for ind,val in enumerate(secret_code):
        if val == my_guess[ind]:
            print('Matched exactly!!')
        elif val in my_guess:
            print('Your answer exists, but not exactly!')

    if answer == []:
        return ['Nope']
    else:
        return answer

def get_guess():
    return list(input('''enter your guessing number!
    '''))

def generate_secret_code():
    sec_code = [str(num) for num in range(10)]
    random.shuffle(sec_code)
    print(sec_code[0:3])
    return sec_code[0:3]

while answer != "WINNER":
    answer = find_answer(generate_secret_code(),get_guess())
    for ans in answer:
        print(ans)
