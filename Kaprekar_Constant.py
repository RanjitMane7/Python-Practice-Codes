'''
Problem Statement : Kaprekar Constant

Have the function KaprekarsConstant(num) take the num parameter being passed which will be a 4-digit number with at least two distinct digits. Your program should perform the following routine on the number: Arrange the digits in descending order and in ascending order (adding zeroes to fit it to a 4-digit number), and subtract the smaller number from the bigger number. Then repeat the previous step. Performing this routine will always cause you to reach a fixed number: 6174. Then performing the routine on 6174 will always give you 6174 (7641 - 1467 = 6174). Your program should return the number of times this routine must be performed until 6174 is reached. For example: if num is 3524 your program should return 3 because of the following steps: (1) 5432 - 2345 = 3087, (2) 8730 - 0378 = 8352, (3) 8532 - 2358 = 6174.
'''

#Kaprekar's Constant

def KaprekarsConstant(num): 
    count = 0
    
    while num != 6174 :
        
        num_list_1 = sorted(list(str(num)))
        print(num_list_1)
        num_list_2 = sorted(list(str(num)), reverse=True)
        print(num_list_2)
        #seq = list(map(int,num_list))
    
        s = ""
        n1 = int(s.join(num_list_1))
        n2 = int(s.join(num_list_2))
        num = abs(n1 - n2) 
        count = count + 1
        
        if num == 6174 :
            break
        
        if num < 1000 :
            num = num * 10
            #print(num)
            #return 0
        
    return count
    
# keep this function call here  
KaprekarsConstant(1011)
