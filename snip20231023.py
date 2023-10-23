# list(s) first then arrays
#
# to use arrays, you must use either:
# arrary module or
# numpy module
# you generally do not need both.
import array as arr
import numpy as np

# lists can be mixed data type items/elements
# import module not required
# create a list of various items/elemets of different types
my_list =  [['w', 'X', 'y', 'Z'], 26, "Sunny", ]

# display the list
# output should be:
# [['w', 'X', 'y', 'Z'], 26, 'Sunny']
print( my_list )

# display the data types
# output should be:
# <class 'list'>
print( type( my_list ) )


# arrarys must be all the same data type
# arrary require an imported module
myArray = arr.array( "i", [64, 128, 256, 256] )
# that "i" is not a string in the arrary.
# the "i" tells arr the data type is integer.
print( myArray )
print(type( myArray ))

