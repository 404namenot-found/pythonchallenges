# A string is a palindrome when it is the same when read backwards.
# For example, the string "bob" is a palindrome. So is "abba". But the string "abcd" is not a palindrome, because "abcd" != "dcba".
# Write a function named palindrome that takes a single string as its parameter. Your function should return True if the string is a palindrome, and False otherwise.

def palindrome(text):
    reversed_word = ""
    index = len(text)
    
    for char in text:
        reversed_word += text[index-1]
        index -= 1
        
    if reversed_word == text:
        return True
    else:
        return False

print(palindrome("kayak"))
print(palindrome("laptop"))
