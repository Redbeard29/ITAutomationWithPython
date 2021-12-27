#Practice quiz using basic string manipulation techniques


#1:
#The is_palindrome function checks if a string is a palindrome. A palindrome is a string that can be equally read 
#from left to right or right to left, omitting blank spaces, and ignoring capitalization. Examples of palindromes are 
#words like kayak and radar, and phrases like "Never Odd or Even". Return True if the passed string is a palindrome, False if not.

def is_palindrome(input_string):
    new_string = ""
    reverse_string = ""

    for char in input_string:
        if char.isalpha():
            new_string = char.lower() + new_string
            reverse_string = reverse_string + char.lower()
    
    if new_string == reverse_string:
        return True
    return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

#2:
#Using the format method, build a convert_distance function so that it returns the phrase "X miles equals Y km", 
#with Y having only 1 decimal place. For example, convert_distance(12) should return "12 miles equals 19.2 km".

def convert_distance(miles):
    km = miles * 1.6
    result = "{} miles equals {:.1f} km".format(miles, km)
    return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

#3:
#create a function called nametage that uses the format method to return first_name and the first initial of 
#last_name followed by a period. For example, nametag("Jane", "Smith") should return "Jane S."

def nametag(first_name, last_name):
    return("{} {:.1s}.".format(first_name, last_name))

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 

#4:
#The replace_ending function replaces the old string in a sentence with the new string, but only if the sentence ends 
#with the old string. If there is more than one occurrence of the old string in the sentence, only the one at the end is 
#replaced, not all of them. For example, replace_ending("abcabc", "abc", "xyz") should return abcxyz, not xyzxyz or xyzabc. 
#The string comparison is case-sensitive, so replace_ending("abcabc", "ABC", "xyz") should return abcabc (no changes made). 

def replace_ending(sentence, old, new):
    sent_arr = sentence.split()
    
    if sent_arr[-1] == old:
        i = sentence.rindex(old)
        new_sentence = sentence[:i] + new
        return new_sentence

    return sentence

print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"