import random

words = ['h', 'a', 'n', 'g', 'm', 'a', 'n']
display = inp = []
flag = 0
chances = 6

que = ['h', 'a', 'n', 'g', 'm', 'a', 'n']
while chances :
    inp.append(input('Enter letter :'))
    if inp[-1] in que :
        flag = 1
    print()

    if flag :
        for i in que :
            if i == inp :
                display.append(i)
            elif i in que :
                continue
            else :
                display.append('_')
        

    for j in display :
        print(j,' ',end = '')

    chances -= 1
