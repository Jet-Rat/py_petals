'''
Created on 2018-03-25

@author: Jet Rat
'''



import sys
import os
import random



##########################################
##  VARS
##########################################

dice_count = 5



##########################################
##  FUNCTIONS
##########################################

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def tell_rules():
    clear_screen()
    print('1) The name of the game is Petals Around the Rose, and the name is significant.')
    print('2) Every answer is zero or an even number.')
    print('3) There is one correct answer for every throw of the dice.')


def generate_combination(dice_count):
    dices = []
    
    while len(dices) < dice_count:
        dices.append(random.randint(1,6))
    
    return dices


def draw_combination(dices):
    dices_pic = list(map(build_dice_pic,dices))
    
    print()
    print('-------------------------------')
    
    for str_num in range(3):
        print('|', end='')
        for dice_num in range(len(dices)):
            print(dices_pic[dice_num][str_num],end='|')
        print()
    
    print('-------------------------------')
    print()


def build_dice_pic(dice_value):
    dice_pic = [None] * 3
    
    if (dice_value == 1):
        dice_pic[0] = '     '
    elif (dice_value < 4):
        dice_pic[0] = '    0'
    else:
        dice_pic[0] = '0   0'
    
    dice_pic[2] = dice_pic[0][::-1]
    
    if (dice_value % 2 == 1):
        dice_pic[1] = '  0  '
    elif (dice_value == 6):
        dice_pic[1] = '0   0'
    else:
        dice_pic[1] = '     '
    
    return(dice_pic)


def ask_for_answer():
    answer = input('How many petals around the rose? (type number or "quit")\n')
    print()
    
    if answer == 'quit':
        quit_game()
    else:
        return answer


def count_solution(dices):
    return sum(list(map(lambda x: ((x % 2) * (x - 1)), dices)))


def tell_solution(answer, solution):

    if answer == str(solution):
        print('Yes, answer is ' + answer)
    else:
        print('Real answer is ' + str(solution))
    
    input()


def quit_game():
    print('See ya!')
    input()
    sys.exit()



##########################################
##  MAIN
##########################################

if __name__ == '__main__':
    
    while True:
        
        tell_rules()
        
        dices = generate_combination(dice_count)
        
        draw_combination(dices)
        
        answer = ask_for_answer()
        
        solution = count_solution(dices)
        
        tell_solution(answer, solution)