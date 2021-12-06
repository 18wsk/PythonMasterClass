computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse pad"
                  ]
print(computer_parts)
print()

computer_parts[3] = "trackball"
print(computer_parts)
print()

print(computer_parts[3:])
computer_parts[3:] = "trackball"
#string is an iterable and will be broken down into its contents..ie- chars
print()

extra_parts = ["controller", "speaker"]
computer_parts[:2] = extra_parts
print(computer_parts)