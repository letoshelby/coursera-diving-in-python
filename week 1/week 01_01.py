import sys

digit_string = sys.argv[1]

sum = 0
for c in digit_string:
    sum += int(c)

print(sum)
