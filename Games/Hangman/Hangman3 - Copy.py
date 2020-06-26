import random
#import os

def login() :
    username = input('If new user, Enter new username, if not, Username : ')
    users = open('users_list.txt')
    users_list = users.read()
    if username not in users_list :
        users.close()
        users = open('users_list.txt','a')
        users.write(username + ',' + '0')
        users.close()
    else :
        print('Welcome',username)
        print('Your points are :',0)

def get_word(choice) :
    word_list = open('word_list.txt','r')
    temp = []
    simple = []
    medium = []
    hard = []

    '''print(simple,'\n---------------')
    print(medium,'\n---------------')
    print(hard,'\n---------------')'''

    content = word_list.read()
    #print(content)
    
    
    for i in content :
        if i.isalpha() :
            temp.append(i.upper())
            continue
        elif i.isspace() :
            if len(temp) > 7 :
                simple.append(temp)
                #print('SIMPLE',simple)
            elif len(temp) > 4 :
                medium.append(temp)
                #print('MED',temp)
            elif len(temp) > 2:
                hard.append(temp)
                #print('HARD',temp)
        #print('\nFlushing :',temp)
        temp = []
        
    word_list.close()

    '''print('\n\n\n*****************************************')
    for l in simple :
        for m in l :
            print(m,end='')
        print(' ')

    #print(simple,'\n---------------')
    #print(medium,'\n---------------')
    #print(hard,'\n---------------')'''

    ss = [simple,medium,hard]    
    return random.choice(ss[choice])

print('*** Welcome to Hangman Game ***')
log = login()
print('Select the level\n1. Low\n2. Medium\n3. High')
level = int(input('\n(Choose 1,2,3) : '))
if level not in (1,2,3) :
    exit()

word = get_word(level-1)
chances = len(word)
k = []
wrong = []


print('- ' * chances)

while chances :
    flag = 1
    inp = input('Guess : ').upper()
    
    if len(inp) != 1 or not inp.isalpha() :
        print('Incorrect input, try again!')
        continue

    if inp in word :
        print('Correct!')
        k.append(inp)
    else :
        chances -= 1
        wrong.append(inp)
        print('Oops... wrong word! \nChances remained :',chances, '\nUsed words :',wrong)

    for i in word :
        if i in k :
            print(i+' ',end = '')
        else :
            print('- ',end = '')
            flag = 0
    print('\n')

    if flag :
        print('You won!\nPoints earned :',chances + 5 * level)
        break
    
if not chances :
    print('You Lost!\nThe answer was :',''.join(word).upper())
