# a set is an unordered collection of unique objects

my_set = {1,2,3,4,5}
# This returns the whole set
print(my_set) 

set2 = {1,2,3,4,5,5,5}
# this will only return {1,2,3,4,5} because sets do not contain duplicate data
print(set2)
# this adds data to the set
set2.add(39)
print(set2)

my_list = [1,2,3,4,5]

my_set = set(my_list)
print(my_set)

set_1 = {1,2,3,4,5}
# This will error because sets are not in order in memory

#print(set_1[0])

# we can only access the information by checking for values within the set for example:

#This prints True because 1 is somewhere within set_1
print(1 in set_1)

#This prints the length of the set starting from a 1 
print(len(set_1))

important_set = {1010,2207}
# this cretes a copy of the important_set
important_set_cp = important_set.copy()
# this clears the contents of important_set
important_set.clear()
# this prints out the copied set
print(important_set_cp)
# this prints out an empty set because important_set is now empty 
print(important_set)