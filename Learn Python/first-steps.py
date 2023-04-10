x = 4
y = 5
z = x + y
print(z)

my_list = ['a', 'b', 'c', 'd']

varied_list = ['a', 1, 'b', 3.14159] # a list with elements of char, integer, and float types
nested_list = ['hello', 'governor', [1.618, 42]] # a list within a list!

second_element = varied_list[1] # Grab second element of varied_list
print(second_element)

last_element = my_list[-1] # the last element of my_list
last_element_2 = my_list[len(my_list)-1] # also the last element of my_list, obtained differently
second_to_last_element = my_list[-2]

NFL_list = ["Chargers", "Broncos", "Raiders", "Chiefs", "Panthers", "Falcons", "Cowboys", "Eagles"]
AFC_west_list = NFL_list[:4] # Slice to grab list indices 0, 1, 2, 3 -- "Chargers", "Broncos", "Raiders", "Chiefs"
NFC_south_list = NFL_list[4:6] # Slice list indices 4, 5 -- "Panthers", "Falcons"
NFC_east_list = NFL_list[6:] # Slice list indices 6, 7 -- "Cowboys", "Eagles"

x = 1
y = 2
coordinates = (x, y)

year1 = 2011
month1 = "May"
day1 = 18
date1 = (month1, day1, year1)
year2 = 2017
month2 = "June"
day2 = 13
date2 = (month2, day2, year2)
years_list = [year1, year2]

#Diccionarios

book_dictionary = {"Title": "Frankenstein", "Author": "Mary Shelley", "Year": 1818}
print(book_dictionary["Author"])

#print(book_dictionary[1])

#For Loops

sum = 0
for i in range(10):
    sum = sum + i
print(sum)
alternative_sum = 0+1+2+3+4+5+6+7+8+9
print(alternative_sum==sum)

ingredients = ["flour", "sugar", "eggs", "oil", "baking soda"]
for ingredient in ingredients:
    print(ingredient)
    
for i in range(10):
    if i % 2 == 0: # % -- modulus operator -- returns the remainder after division
        print("{} is even".format(i))
    else:
        print("{} is odd".format(i))  
    
# Example using elif as well
# Print the meteorological season for each month (loosely, of course, and in the Northern Hemisphere)
print("In the Northern Hemisphere: \n")
month_integer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] # i.e., January is 1, February is 2, etc...
for month in month_integer:
    if month < 3:
        print("Month {} is in Winter".format(month))
    elif month < 6:
        print("Month {} is in Spring".format(month))
    elif month < 9:
        print("Month {} is in Summer".format(month))
    elif month < 12:
        print("Month {} is in Fall".format(month))
    else: # This will put 12 (i.e., December) into Winter
        print("Month {} is in Winter".format(month))
    
#List comprension    
    
even_list = [2, 4, 6, 8]
odd_list = [even+1 for even in even_list]
print(odd_list)

#NumPy Lireria

import numpy as np 

x = np.array([2, 4, 6]) # create a rank 1 array
A = np.array([[1, 3, 5], [2, 4, 6]]) # create a rank 2 array
B = np.array([[1, 2, 3], [4, 5, 6]])

print("Matrix A: \n")
print(A)

print("\nMatrix B: \n")
print(B)

# Indexing/Slicing examples
print(A[0, :]) # index the first "row" and all columns
print(A[1, 2]) # index the second row, third column entry
print(A[:, 1]) # index entire second column

# Arithmetic Examples
C = A * 2 # multiplies every elemnt of A by two
D = A * B # elementwise multiplication rather than matrix multiplication
E = np.transpose(B)
F = np.matmul(A, E) # performs matrix multiplication -- could also use np.dot()
G = np.matmul(A, x) # performs matrix-vector multiplication -- again could also use np.dot()

print("\n Matrix E (the transpose of B): \n")
print(E)

print("\n Matrix F (result of matrix multiplication A x E): \n")
print(F)

print("\n Matrix G (result of matrix-vector multiplication A*x): \n")
print(G)

# Broadcasting Examples
H = A * x # "broadcasts" x for element-wise multiplication with the rows of A
print(H)
J = B + x # broadcasts for addition, again across rows
print(J)

# max operation examples

X = np.array([[3, 9, 4], [10, 2, 7], [5, 11, 8]])
all_max = np.max(X) # gets the maximum value of matrix X
column_max = np.max(X, axis=0) # gets the maximum in each column -- returns a rank-1 array [10, 11, 8]
row_max = np.max(X, axis=1) # gets the maximum in each row -- returns a rank-1 array [9, 10, 11]

# In addition to max, can similarly do min. Numpy also has argmax to return indices of maximal values
column_argmax = np.argmax(X, axis=0) # note that the "index" here is actually the row the maximum occurs for each column

print("Matrix X: \n")
print(X)
print("\n Maximum value in X: \n")
print(all_max)
print("\n Column-wise max of X: \n")
print(column_max)
print("\n Indices of column max: \n")
print(column_argmax)
print("\n Row-wise max of X: \n")
print(row_max)

# Sum operation examples
# These work similarly to the max operations -- use the axis argument to denote if summing over rows or columns


total_sum = np.sum(X)
column_sum = np.sum(X, axis=0)
row_sum = np.sum(X, axis=1)

print("Matrix X: \n")
print(X)
print("\n Sum over all elements of X: \n")
print(total_sum)
print("\n Column-wise sum of X: \n")
print(column_sum)
print("\n Row-wise sum of X: \n")
print(row_sum)

# Matrix reshaping

X = np.arange(16) # makes a rank-1 array of integers from 0 to 15
X_square = np.reshape(X, (4, 4)) # reshape X into a 4 x 4 matrix
X_rank_3 = np.reshape(X, (2, 2, 4)) # reshape X to be 2 x 2 x 4 --a rank-3 array
                                    # consider as two rank-2 arrays with 2 rows and 4 columns
print("Rank-1 array X: \n")
print(X)
print("\n Reshaped into a square matrix: \n")
print(X_square)
print("\n Reshaped into a rank-3 array with dimensions 2 x 2 x 4: \n")
print(X_rank_3)

#Plotting

#import numpy as np
import matplotlib.pyplot as plt

# We'll start with a parabola
# Compute the parabola's x and y coordinates
x = np.arange(-5, 5, 0.1)
y = np.square(x)

# Use matplotlib for the plot
plt.plot(x, y, 'b') # specify the color blue for the line
plt.xlabel('X-Axis Values')
plt.ylabel('Y-Axis Values')
plt.title('First Plot: A Parabola')
plt.show() # required to actually display the plot

import numpy as np
import matplotlib.pyplot as plt

X = np.identity(10)
identity_matrix_image = plt.imshow(X, cmap="Greys_r")
plt.show()

# Now plot a random matrix, with a different colormap
A = np.random.randn(10, 10)
random_matrix_image = plt.imshow(A)
plt.show()



