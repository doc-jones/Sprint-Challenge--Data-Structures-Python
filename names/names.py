import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

#duplicates = []
#for name_1 in names_1:
#    for name_2 in names_2:
#        if name_1 == name_2:
#            duplicates.append(name_1)

bst = BinarySearchTree(names_1[0]) 

for name in names_1[1:]: # iterate through names_1 from begining to end
    bst.insert(name)  # add to BST
duplicates = []
for name in names_2:
    if bst.contains(name):  # compare name in names_2 with bst of names_1
        duplicates.append(name) # add name found in both to duplicates[]


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

