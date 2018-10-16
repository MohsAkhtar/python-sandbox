# A List is a collection which is ordered and changeable. Allows duplicate members.
# Basically an array

# Create list
numbers = [1,2,3,4,5]

#Create using a constructor
numbers = list((1,2,3,4,5))

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Get value
print(fruits[1])    # Oranges

# Get length 
print(len(fruits))  # 4

# Append to list
fruits.append('Mangos')

# Remove from list
fruits.remove('Grapes')

# Insert into position
fruits.insert(2, 'Strawberries')

# Remove from certain position
fruits.pop(3)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)