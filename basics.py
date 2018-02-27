 start_list = [5, 3, 1, 2, 4]
square_list = []

for n in start_list:
  square_list.append(n ** 2)
  square_list.sort()

print square_list

inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50


def divisions(n, divisor):
  count = 0
  current = n
  if current / divisor > 1:
      print "check"
      count = count + 1
      current = current / divisor
  else:
      return count