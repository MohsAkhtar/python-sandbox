# Python has functions for creating, reading, updating, and deleting files.

# Open a file - w = write
myFile = open('myfile.txt', 'w')

# Get some info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.close()

# Append to file - a = append
myFile = open('myfile.txt', 'a')
myFile.write(' I also like JavaScript')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(10)
print(text)             # print fist 10 chars of file