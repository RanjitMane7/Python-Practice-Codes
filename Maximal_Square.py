"""
Challenge - Have the function MaximalSquare(strArr) take the strArr parameter being passed which will be a 2D matrix of 0 and 1's, and determine the area of the largest square submatrix that contains all 1's. A square submatrix is one of equal width and height, and your program should return the area of the largest submatrix that contains only 1's. For example: if strArr is ["10100", "10111", "11111", "10010"] then this looks like the following matrix: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0 

For the input above, you can see the bolded 1's create the largest square submatrix of size 2x2, so your program should return the area which is 4. You can assume the input will not be empty. 

Sample Test Cases
    Input:"0111", "1111", "1111", "1111"
    Output:9

    Input:"0111", "1101", "0111"
    Output:1

Problem : 
0111
1111
1111
1111
output = 9


0 1 1 1
1 1 0 1
0 1 1 1
output = 1
"""


#input = ["0111", "1101", "0111"] > ok 
#input = ["0111", "1111", "1111", "1111"] ok 
#input = ["10100", "10111", "11111", "10010"] ok
input = ['0111111111','1111111111','1111111111','1111111111','1111111111','1111111111','1111111111','1111111111''1111111111','1111111111'] #64
#input = ['111','111','111'] 

## Checking the square of length adder from the given position
def sq_checker(n,m,adder) :
    print('>> in sq_checker')
    print('adder : ' + str(adder) + ' Input n,m : ' + str(input[n][m]))

    if adder == 0 and input[n][m] == str(1) :
        print('Returning 1')
        return 1
    else :
        columns_list = range(m,m+adder+1)
        rows_list = range(n,n+adder+1)
        
    
    for i in rows_list :
        #print('Checking i =' + str(i))
        for j in columns_list :
            print('Checking i,j = ' + str(i) + ',' + str(j) + ' : ' + str(input[i][j]))
            if input[i][j] != '1' :
                print('Here ' + str(i) + ',' + str(j) + ' is 0. So returing 00000000000000000000')
                return 0
            #elif  :
            
    print('Returning adder+1 : ', str(adder + 1))
    return adder+1


#print(sq_checker(0,0,3))





#This function will go through the input and check for the maximal square
def travel(input) :
    rows = len(input)
    columns = len(input[0])
    maxc = 0
    i = j = 0
    
    for i in range(0,rows+1) :
        for j in range(0,columns+1) :
            
            if maxc + i <= rows and maxc + j <= columns :
                i = j = 0
                print('\n *** Travelling : '+ str(i) + str(j))
                result = sq_checker(i,j,maxc)
            #maxc = result
                if maxc < result :
                    maxc = result
                    #i = j = 0
                    #maxc += 1
                    print('\n*** \nMaxc == Result == ' + str(maxc) + '\n***')
                    print('i : ' + str(i) + '\tj : ' + str(j))      
                        
            '''if maxc < rows and maxc < columns :
                print("Passing values : " + str(i) + ',' + str(j) + ' ' + str(maxc))
                result = sq_checker(i,j,maxc)
                print("Result : " + str(result))
                if result >= 0 :
                    print('********** Inside IF')
                    maxc += result
                    print("Maxc :" + str(maxc) + '\n')
                    #sq_checker(i,j,maxc)'''

    return maxc * maxc


print ("Result is : " + str(travel(input)))




















































    
