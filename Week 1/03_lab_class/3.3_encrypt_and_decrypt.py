""" 
Encrypt the following code so that no one can get your stategy

"""

data = "firebaby"

shift = 4

output = ''

for character in data:
  output += chr((ord(character)+shift-97) % 26 +97)

print(output)