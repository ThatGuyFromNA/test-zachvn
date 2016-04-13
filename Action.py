# -------------------------------------------------------------------------------

# Name:           ICS4U_Assignment 2_2_Zachary van Noppen.py

# Purpose:        This is a program that will allow the user to create 2D matrixes, transpose them and then see if they are symetrical

#

# Author:         van Noppen. Z.

#

# Created:        31/03/2016

#    

# ------------------------------------------------------------------------------

import random

#defining gloabal variables
user_in = 0
user_t = ""
user_bool = False
my_matrix = []
transposed_matrix = []

#creating a function to make the matrixes
def create_matrix(num):
    temp_matrix = []
    global my_matrix
    my_matrix = []
    n = 0   
    #creating the number of lists that matches the criteria and filling those lists with random numbers
    while n < num:
        i = 0
        temp_matrix = [None]*num
        
        while i < num:
            temp_matrix[i] = random.randint(0,10)
            i += 1
        #putting all the lists in one list    
        my_matrix.append(temp_matrix)            
        n+=1
    
    print "Your matrix is : ", my_matrix
    return my_matrix

#creating a function to test if the matrix is symmetrical    
def is_symmetric(matrix,t_matrix, num):
    i = 0
    sym_count = 0
    #testing to see if the individual lists are equal
    while i < num:
        if matrix[i] == t_matrix[i]:
            sym_count += 1
        i += 1   
    #returning if it is symmetrical or not    
    if sym_count == num:
        return True
    
    else:
        return False

#creating a function that transposed the matrix
def transpose(matrix):
    
    global transposed_matrix
    tuple_matrix = []
    #the zip function will unpack the matrix. Because it always has the same number of rows and columns it will act to transpose it
    tuple_matrix = zip(*matrix) 
    t = []  
    #converting the transposed matrix from the tuple format to the list format
    for i in tuple_matrix:
        t = list(i)
        #adding each individual list to the matrix
        transposed_matrix.append(t)
        
    return transposed_matrix

#creating a function to determine if the user has inputted valid data
def y_or_n(string):
    if user_t == "y":
        global user_bool
        user_bool = True
    elif user_t == "n":
        user_bool = True
    else:
        user_bool == False  
    return user_bool

#making sure the user input is valid
user_in = raw_input("Enter a number that will create a maxtrix : ")
while int(user_in) <= 0:
    user_in = raw_input("The input is invalid. Please enter a positive number : ")



#creating, transposing and testing the matrix for symmetry    
create_matrix(int(user_in))
transpose(my_matrix)
#is_symmetric(my_matrix, transposed_matrix, int(user_in))

#telling the user if the matrix is symmetrical or not
if is_symmetric(my_matrix, transposed_matrix, int(user_in)) == True:
    print "Your matrix is symmetrical"
else:
    print "Your matrix is not symmetrical"

#getting user input
user_t = raw_input("Would you like to transpose the matrix? y/n : ")

#seeing if the user data is valid
y_or_n(user_t)

#making sure the user inputs valid data
while user_bool == False:
    user_t = raw_input("Your input is invalid. Answer 'y' or 'n' : ")
    y_or_n(user_t)    

#determining if the user wants to transpose the matrix
if str(user_t) == "y":
    print "Your transposed matrix is ", transposed_matrix
    print "Ending the program..."
else:
    print "Okay, ending the program..."

    
#this script shows that the is_symmetric() method works. It passes a symmetrical list through the method.
#take it out of the comment section and it will run at the end of the program.

transposed_matrix = []
m = [[2,9,1],[9,3,7],[1,7,6]]
print "The original matrix is : ", m, "and the transposed matrix is", transpose(m)
print "They are the same! Therefore, is 'is_symmetric()' is ", is_symmetric(m, transpose(m), 3)

p = 2
if p == 1:
    print " "
elif p == 2:
    print "THIS IS A CHANGE FOR DURING CLASS!"