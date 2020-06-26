import random


word_list = ['hangman']


print('***** Welcome to Hangman *****')


#Function to display current status.
def display(que) :
    if not part_ans  :
        part_ans = '-' * len(que)
    print(part_ans)

#Select a word for the current game (Randomly)
def choose_word() :
    return random.choice(word_list)

end = 1
chances = 6
part_ans = []
an = []

while end and chances :
    que = choose_word().split('')
    an.append(input('Type character :'))
    print('que',que)

    if an in que :
        for i in que :
            if an == i :
                part_ans.append(an)
            else :
                part_ans.append('_')
    else :
        print('Oops..!')
        chances -= 1

    print(''.join(part_ans))
        
            
    #print(part_ans)
    #end = 0
