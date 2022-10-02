# Complete the organizingContainers function in the editor below.

# organizingContainers has the following parameter(s):

# int containter[n][m]: a two dimensional array of integers that represent the number of balls of each color in each container

# Returns string: either Possible or Impossible



def organizingContainers(container):
    caps = []
    for i in range(len(container)):
        caps.append(sum(container[i]))
    typenums = []
    for i in range(len(container)):
        n = 0
        for j in range(len(container)):
            n += container[j][i]
        typenums.append(n)
    
    if sorted(caps) == sorted(typenums):
        return 'Possible'
    else:
        return 'Impossible'
