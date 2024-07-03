import sys

# Grabbing input
n = input('Please set a whole number value for n between 1 and 50\n')
print(' ')

# Checking input is an int, exit if not
try:
    n = int(n)

except ValueError:
    print('Error:', n, 'is not a whole number!')
    sys.exit()

# Main loop, if else statment checks if the number is between 1 and 50 (50 chosen as when running this fullscreen it starts to get weird higher than that)
n = int(n)
if 0 < n < 51:
    print('You have requested for a', n, 'by', n, 'box, constructing now.\n')

    for i in range(n):
        if i in (n-1, 0):
            for j in range(n):
                print('#', end = ' ')
        else:
            for j in range(n):
                if j in (n-1, 0):
                    print('#', end = ' ')
                else:
                    print(' ', end = ' ')
        print(' ')

    # Printing a statement returning their box dimensions
    print(' ')
    print('Here is your', n, 'by', n, 'box!')

# Handling numbers outside of the range 1-50
else:
    print('Error:', n, 'is less than 1 or greater than 50')
