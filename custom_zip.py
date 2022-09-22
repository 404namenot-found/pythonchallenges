# The built-in zip function "zips" two lists. Write your own implementation of this function.
# Define a function named zap. The function takes two parameters, a and b. These are lists.
# Your function should return a list of tuples. Each tuple should contain one item from the a list and one from b.
# You may assume a and b have equal lengths.

def zap(list1, list2):
    final_list = []
    list_len = len(list1)
    x = 0
    
    while x<list_len:
        final_list.append((list1[x],list2[x]))
        x += 1
    
    return final_list
