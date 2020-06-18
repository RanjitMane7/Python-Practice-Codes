'''
Problem Statement : Correct Path

Have the function CorrectPath(str) read the str parameter being passed, which will represent the movements made in a 5x5 grid of cells starting from the top left position. The characters in the input string will be entirely composed of: r, l, u, d, ?. Each of the characters stand for the direction to take within the grid, for example: r = right, l = left, u = up, d = down. Your goal is to determine what characters the question marks should be in order for a path to be created to go from the top left of the grid all the way to the bottom right without touching previously travelled on cells in the grid.

For example: if str is "r?d?drdd" then your program should output the final correct string that will allow a path to be formed from the top left of a 5x5 grid to the bottom right. For this input, your program should therefore return the string rrdrdrdd. There will only ever be one correct path and there will always be at least one question mark within the input string.
'''

'''
1. For the input "r?d?drdd" your output was incorrect. The correct answer is rrdrdrdd.
2. For the input "???rrurdr?" your output was incorrect. The correct answer is dddrrurdrd.
3. For the input "drdr??rrddd?" your output was incorrect. The correct answer is drdruurrdddd.
4. For the input "rrrr????" your output was incorrect. The correct answer is rrrrdddd.
5. For the input "ddd?uru??ddd" your output was incorrect. The correct answer is dddrururrddd.
6. For the input "rd?u??dld?ddrr" your output was incorrect. The correct answer is rdrurrdldlddrr.
7. For the input "dddd?uuuurrr????" your output was incorrect. The correct answer is ddddruuuurrrdddd.
8. For the input "ddr?rdrrd?dr" your output was incorrect. The correct answer is ddrurdrrdldr.
9. For the input "rdrdrdr?" your output was incorrect. The correct answer is rdrdrdrd.
10. For the input "rdrdr??rddd?dr" your output was incorrect. The correct answer is rdrdruurdddldr.
'''



import random

#inn = "r?d?drdd" #9
#inn = "???rrurdr?" #773
#inn = "drdr??rrddd?" 2
#inn = "rrrr????" #669
#inn = "ddd?uru??ddd" #9
#inn = "dddd?uuuurrr????" #432
#inn = "ddr?rdrrd?dr" #0
inn = "rdrdrdrd" #3
#inn = "rdrdr??rddd?dr" #23

#inn = '????????' #worst case ~7500



#count_x = count_y = count_q =0
#ans = ''



def trial() :
    ans = ''
    for i in inn :
        if i == '?':
            i = random.choice('lrud')
            #i = 'r'
        ans += i
    print(ans)
    return ans


def counter_x(sample) :
    countx = 0
    for i in sample :
        if i == 'r' :
            countx += 1
        elif i == 'l' :
            countx -= 1
    return countx


def counter_y(sample) :
    county = 0
    for i in sample :
        if i == 'd' :
            county += 1
        elif i == 'u' :
            county -= 1
    return county

#print('counts LRUDQ :',count_x,count_y)
#print('Question',inn)
#print('Answer',ans)

m = count_x = count_y = 0

while count_x != 4 or count_y != 4 :
    print('Try :', m)
    answer = trial()
    count_x = counter_x(answer)
    count_y = counter_y(answer)
    m += 1


print('Got it -', answer)













'''
## function to return the next position based on passed direction (LRTB)
def goto_position(current_pos, side) :
    if side == 'l':
        return current_pos - 1
    if side == 'r':
        return current_pos + 1
    if side == 'u':
        return current_pos - 10
    if side == 'd':
        return current_pos + 10
#print(goto_position(22,'d')


## function to return whether the passed path is reaching the destination or not
def travelar(path) :
    pos = 00
    for i in path:
        pos = goto_position(pos,i)
        #print('position : ' + str(pos))

    if pos == 44 :
        return 1
    else :
        return 0

print('Final check',travelar(answer))
'''
