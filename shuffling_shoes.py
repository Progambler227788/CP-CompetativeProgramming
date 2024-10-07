# import sys
# sys.stdout = open('D:/CP/output.txt','w')  
# sys.stdin = open('D:/CP/input.txt','r')
#NOTE:
# Ignore above lines that are meant to be manual testing on IDE via files
def predictShuffle(students,sizes):

   

    #********************INVENTORY****************

    # shuffling_shoes_students  is a map/dictionary to store keys and elements, in c++ there is unordered_map in STL
    # shuffling_shoes_students  is serving as INVENTORY
    
    shuffling_shoes_students = {} # to store keys as elements

    # Our array is in nondecreasing order, it means sizes will either keep repeating or increase 1 1 1 2 2 2 2 3 3 3 3

    
    #********************CASES:****************

    # Wrong Cases
    # a) 1 2 3 4 5, -1 as 5 can't have another 5 or 6 >= scenario to be in mind
    # b) 1 2 2 3 3, now 1 will not be taken by either 2 or 3 so that would be also -1

    # Correct Cases
    # a) 1 1 1 1 1, all are same size so good to go and return order in shuffling, that is case where all elements are 1
    # b) 2 2 3 3 4 4 even number of repeated numbers, why correct because? shuffling can be made. 0 indexed 2 and 1 indexed 2 exchanges shoes with each other
    # c) 2 2 2 3 3 3 4 4 4 odd number of repeated numbers, why correct, think it like we did in a), Indexes key with indexes value

    #  First -> 0, Second -> 1, Third -> 3
    #  exchange pairs (0-2)-> 0 first student , 2 last student  
    #  exchange pairs (1-0)-> 1 second student, 0 first student  
    #  exchange pairs (2-1)-> 2 third student , 1 second student  
    # Similarly, you will do for 3 and 4. 
    # So, you have to do that in parts of array
    

    #********************My Logic of Returning Shuffled ORDER, YOUR MAY CHANGE****************
    # In my solution, I've returned answer according to test case explanation as next student will take sizes from previous one
    # Values 1 1 1 1, Indexes -> 0,1,2,3 -> 3,0,1,2 so programmatically it is array of last element + remaning elements
    # Last element + elements from 1 to n - 2 , n is size of array. As we are dealing with indexes so it is n - 2, skipping last element
    # In python, range function iterates from starting point to ending point -1 like 1-5 will be -> 1,2,3,4

   #********************THOUGHT PROCESS****************
    # During this problem, I tried to think like what will happen in case of 1 2 2 , even same elements, and in same case odd case
    # 1,2,2 and 1,2,2,2 both are -1, so I got that even-odd does not matter, real enemy is here 1, 
    # You can think of this problem like Babar Azam was a junior and his akmal brothers do not gave him shoes why due to his low standard at time
    # Here 1 is bechara person, he has no partner whom he can share his shoes, feeling sad for him 



    # iterate over each student size, i is size of students shoes
    # If size is already in inventory, just append new index of that size otherwise store it in inventory with initial index


    # 1 1 1 1 1

    # 1 2 3 4 5 , invalid
    # 

    for i in range(students):      # loop to store indexes of each size
        if sizes[i] not in shuffling_shoes_students:
            shuffling_shoes_students[ sizes[i] ] = [i]
        else:  
         shuffling_shoes_students[ sizes[i] ].append(i)
    # If there is any key with frequency

    
    for key in shuffling_shoes_students:
        if len( shuffling_shoes_students[key] ) == 1:# short hand# if any(len(value) == 1 for value in shuffling_shoes_students.values()):
           print(-1) # InVALID CASE
           return
        
    # In case of correct, we have to return Correct Permutation 
    result = [] # 1 Dimensional List to store ALL shuffled indexes

    # For each repeated size, it will make array and then add it to result
    for key in shuffling_shoes_students:
        # Sizes of Shoes are keys
        values = shuffling_shoes_students[key]
        # fetch last value and make a new shuffled list
        #  [int(values[-1]) + 1] Picking up last value of array 
       
        data =  [int(values[-1]) + 1] + [ (int(values[x])+1) for x in range(0, len(values) - 1) ] 
        result.extend(data) 
    # You may think * is pointer, but in Python it is Separable Operator that is used to unpack items of a list
    # It will unpack them and will print them space by space, every element is passed to print function as a single integer
    print(*result)
        

testCases = int(input())
# read test cases 
for t in  range(testCases):
    # Read number of students
    students =  input()
    students = int(students)
    # read their total sizes, 0 index -> 1 , 1 index -> 1 so on
    taken = input() # taken as input string
    sizes = taken.split() # spaces removed
    for i in range(len(sizes)):
        sizes[i] = int(sizes[i])

    predictShuffle(students,sizes) 
    
