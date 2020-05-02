age = input('Enter your age: ')

# This age variable is a string, because the input() method always returns a string.

# Then, print out the information to the user.
# Here we use the format() method to replace each pair of curly braces
#       for each argument of the format() method (separated by commas).

print("You have lived for {} seconds. This corresponds to {} years.".format(int(age) * 365 * 24 * 60 * 60, age))
