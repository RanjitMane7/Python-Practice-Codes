'''
Problem Statement : Closest Enemy II

Have the function ClosestEnemyII(strArr) read the matrix of numbers stored in strArr which will be a 2D matrix that contains only the integers 1, 0, or 2. Then from the position in the matrix where a 1 is, return the number of spaces either left, right, down, or up you must move to reach an enemy which is represented by a 2. You are able to wrap around one side of the matrix to the other as well. For example: if strArr is ["0000", "1000", "0002", "0002"] then this looks like the following:

0 0 0 0
1 0 0 0
0 0 0 2
0 0 0 2

For this input your program should return 2 because the closest enemy (2) is 2 spaces away from the 1 by moving left to wrap to the other side and then moving down once. The array will contain any number of 0's and 2's, but only a single 1. It may not contain any 2's at all as well, where in that case your program should return a 0.
'''


#Input:"000", "100", "200"
#Output:1

#Input:"0000", "2010", "0000", "2002"
#Output:2


#inn = [[0,0,0,0], [2,0,1,0], [0,0,0,0], [2,0,0,2]]
#inn = [[0,0,0], [1,0,0], [2,0,0]]
inn = [[0,0,0,2], [1,0,0,0], [0,0,0,2], [0,0,0,2]] 
pos_2 = []
distance = []


for s in inn :
    print(s)


ir = 0
for i in inn :
    #print(i)
    jr = 0
    for j in i :
        #print(j)
        if j == 1 :
            pos_1 = [ir,jr]
        if j == 2 :
            #print('j=2')
            #print('inn.index(i)',ir)
            #print('i.index(j)',jr)
            pos_2.append([ir,jr])
        jr += 1
    ir += 1

print('pos_1',pos_1)
print('pos_2',pos_2)


for i in pos_2 :
    diff0 = abs(i[0] - pos_1[0])
    if (len(inn) / 2) < diff0 :
        diff0 = len(inn) - diff0
    print(diff0)

    diff1 = abs(i[1] - pos_1[1])
    if (len(inn[0]) / 2) < diff1 :
        diff1 = len(inn[0]) - diff1
    print(diff1)

    print('diff0,diff1',diff0,diff1)
    print('Total distance of ',pos_1,i,':',diff0 + diff1)
    distance.append(diff0 + diff1)

if pos_2 == [] :
    print('0')

print(min(distance))


