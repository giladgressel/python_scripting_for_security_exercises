# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."
grapes=s[5:9]+s[11:12]
print(grapes)
text_splitted=s.split()
print(text_splitted[10])
desert=text_splitted[10][0:6]
print(desert)