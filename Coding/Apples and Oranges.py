# I am just completing the function guys. please do read input if not given

# Complete the countApplesAndOranges function in the editor below. 
# It should print the number of apples and oranges that land on Sam's house, each on a separate line.

# countApplesAndOranges has the following parameter(s):

# s: integer, starting point of Sam's house location.
# t: integer, ending location of Sam's house location.
# a: integer, location of the Apple tree.
# b: integer, location of the Orange tree.
# apples: integer array, distances at which each apple falls from the tree.
# oranges: integer array, distances at which each orange falls from the tree.


def countApplesAndOranges(s, t, a, b, apples, oranges):
    acount=0
    for i in apples:
        if s<=a+i<=t:
            acount+=1
    ocount=0
    for i in oranges:
        if s<=b+i<=t:
            ocount+=1
    print(acount)
    print(ocount)
