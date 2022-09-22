# Write a function named mid that takes a string as its parameter. 
# Your function should extract and return the middle letter. If there is no 
# middle letter, your function should return the empty string.

def mid(text):
    if len(text)%2==0:
        return ""
    else:
        return text[(len(text)-1)//2]

print(mid("text"))
print(mid("texts"))
