import random
import time

def linear_search(lookingfor, vals):
    return False

def binary_search(lookingfor, vals):
    return False

# --- Main program ------------------------
s = input('Enter list length: ')
size = int(s)

# -- Make a sorted list of random numbers
#numlist = [ 0 for _ in range(int(size))]
#total = 0
#for i in range(size):
#    total = total + int(random.random() * 5)
#    numlist[i] = total

numlist = []
total = 0
for i in range(size):
    total = total + int(random.random() * 5)
    numlist.append(total)

# -- Run and time one of the algorithms
done = False
while not done:
    s = input('Enter a number to find: ')
    if s == "quit" or s == "done":
        done = True
    else:
        val = int(s)
        t1 = time.time()
        found = linear_search(val, numlist)
        t2 = time.time()
        print("Result is " + str(found))
        print("Time: {:08.6f}".format(t2 - t1))
