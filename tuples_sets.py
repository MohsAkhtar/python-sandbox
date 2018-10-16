# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Simple tuple
fruit_tuple = ('Apple', 'Orange', 'Mango')

# Create tuple using a constructor
fruit_tuple = tuple(('Apple', 'Orange', 'Mango'))

# Get a single value
print(fruit_tuple[1])

# You cannot change values of tuples
fruit_tuple[1] = 'Grape'        # error

# Tuples with one value should have trailing comma
fruit_tuple_2 = ('Apple',)

# Get length
print(len(fruit_tuple))

# Delete tuple
del fruit_tuple


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruit_set = {'Apple', 'Orange', 'Mango'}

# Check if in set
print('Apples' in fruit_set)

# Add to set
fruit_set.add('Grape')

# Remove from set
fruit_set.remove('Grape')

# Clear set
fruit_set.slear()

# Delete set
del fruit_set