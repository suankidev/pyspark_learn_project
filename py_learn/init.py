# it will print new line after the messages
print("Hello")
print("World")

# it will print new line
print()

# it will print new line after printing "Hello"
print("Hello",end="\n")
# it will print new line after printing "World"
print("World")

# it will print new line
print()

# it will not print new line after printing "Hello"
# it will print space " "
print("Hello",end=" ")
# it will print new line after printing "World"
print("World")

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print(' ')
print(" ")
print("Hello world!")
print("Hello         world")
print("____________________________________________")
space = ' '

'''
  3 spaces would be here
  1 space after first parameter,
  1 space by using space variable
  1 space after second parameter
'''
print("Hello",space,"world")
'''
  7 spaces would be here
  1 space after first parameter,
  5 space by using space*5
  1 space after second parameter
'''
print("Hello",space*5,"world")

'''
  12 spaces would be here
  1 space after first parameter,
  10 space by using space*10
  1 space after second parameter
'''
print("Hello",space*10,"world")

# for better better understanding
# assign space by any other character
# Here, I am assigning '#'
space = '#'
print("Hello",space,"world")
print("Hello",space*5,"world")
print("Hello",space*10,"world")