# Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".
# Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, 
# calling remove_dots("t.e.s.t") should return "test".
# If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.

def add_dots(text):
    final_string = ""
    counter = 0
    
    for char in text:
        final_string += char
        counter += 1
        
        if counter < len(text):
            final_string += "."
    
    return final_string

def remove_dots(text):
    final_string = ""
    
    for char in text:
        if char != ".":
            final_string += char
        
    return final_string

print(add_dots("test"))
print(remove_dots("t.e.s.t"))
