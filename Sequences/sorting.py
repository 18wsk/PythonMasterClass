pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)
#sorts list into alphabetical order (capitals have priority)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
#CREATES A NEW LIST AND LEAVES THE OG UNCHANGED
print(sorted_numbers)
print(numbers)

print()

numbers.sort()
print(numbers)
print(sorted_numbers)

missing_letter = sorted("The quick brown fox jumps over the lazy dog",
                        key=str.casefold) #dont include () !!!!!
#argument to sort regardless of capitalization
#you can pass a string literal through the function ^
print(missing_letter) #s is missing so it is not a pangram

names =  ["Graham",
          "John",
          "terry",
          "eric",
          "Terry",
          "michael"]

names.sort(key=str.casefold)
print(names)

