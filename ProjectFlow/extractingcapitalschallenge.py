quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
caps = ""
for char in quote:
    if char.isupper(): #returns true if characters are capitalized
        caps = caps + char
print(caps)

#or could do --> if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"