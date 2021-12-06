# Write a program to append the times tables to our jabberwocky poem
# in sample.txt. We want the tables from 2 to 12 (similar to the output
# from the For loops part 2 lecture in section 6

# The first column of numbers should be right justified

with open("sample.txt", "a") as sample_text:
    for i in range(0, 13):
        for j in range(0, 13):
            print("{:>2} times {:<2} is {:<3}".format(j, i, i * j),
                  file=sample_text)
        print("-" * 40, file=sample_text)
