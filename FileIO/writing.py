# cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydeney"]
#
# with open("cities.txt", 'w') as city_file:  # 'w' -> is keyword for writing
#     for city in cities:
#         print(city, file=city_file)
#
# cities = []
#
# with open("cities.txt", 'r') as city_file:
#     for city in city_file:
#         cities.append(city.strip('\n'))  # strips new line character
#
# print(cities)
# for city in cities:
#     print(city)
########################################################################
imelda = "More Mayhem", "Imelda May", "2011", (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

with open("imelda.txt", 'w') as imelda_file:
    print(imelda, file=imelda_file)

with open("imelda.txt", 'r') as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents)
#eval() allows you to evaluate arbitrary Python expressions from a string-based or compiled-code-based input

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)