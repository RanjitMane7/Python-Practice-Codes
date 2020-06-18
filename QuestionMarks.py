'''
Problem Statement : Question Marks

Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. If so, then your program should return the string true, otherwise it should return the string false. If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.
'''


#Input:"aa6?9"
#Output:"false"

#Input:"acc?7??sss?3rr1??????5"
#Output:"true"



'''
For the input "9???1???9??1???9" your output was incorrect. The correct answer is false.
For the input "5??aaaaaaaaaaaaaaaaaaa?5?5" your output was incorrect. The correct answer is false.
'''

check = count = k = 0

#inn = "acc?7??sss?3rr1??????5"
#inn = "aa6?9"
inn = "9???1???9??1???9"

for i in inn :
    print('\n',i)

    if i.isalpha() :
        print('Alpha Continueing')
        continue

    if count == 3 :
        if i == '?' :
            print('Settting check to 0.')
            check = 0
            continue
        '''
        print('count is 3, setting check 0')
        check = count = 0
        print('----------------')
        #final = 1'''
    
    if check :
        print('in Check 1 :', count)
        if i == '?' :
            count += 1
            print('Increasing count :',count)
            #if count > 3 :
            #check = count = 0
                #final = 0
            print('ContinueCount')
            continue
        print('check passed ?')
            
    if i.isnumeric() :
        print('It Numeric',i)
        if count == 3 :
            if int(i) + int(k) == 10 :
                print('Done-----Passed')
                break
        print('Setting i in k===',k,i)
        k = i
        check = 1
        print('k is now :',k)
        continue
    
