# # Instructions

## Determine the sum of all the even number. you've given a list of ints called numbers.
# Your Task: Find all the even numbers in the list called numbers, and then add all those even numbers together.
# Return the sum(All the evens added together)

numbers = [62, 66, 94, 97, 25, 11, 68, 54, 48, 67]

total = 0

for number in numbers:
    # print(number)
    remainder = number % 2
    if remainder == 0:
        total = total + number

print(total)