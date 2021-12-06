# create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialize a string variable with the string

user_in = input("Please Enter Text Below: \n ")
vowels = frozenset("aeiou ")
non_vowels = set(user_in).difference(vowels)

final_set = sorted(non_vowels)
print(final_set)
