flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Tiger Lily",
]
# for flower in flowers:
#     print(flower)
separator = " | "
output = separator.join(flowers)
print(output)
# give join and iterable and it joins all items in iterable
# uses string we call upon as separator
# ALL ITEMS IN ITERABLE MUST BE STRINGS TO BE JOINED

print(", ".join(flowers))