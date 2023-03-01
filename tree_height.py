# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    heightArr = [-1]

    def scan(node):
        if heightArr[node] != -1:
            return heightArr[node]
        if parents[node] == -1:
            heightArr[node] = 1
            return int(1)

        parentHeight = scan(parents[node])

        heightArr[node] = parentHeight

        return heightArr[node]

    # Write this function
    max_height = 0
    for node in range(n):
        heightCurrent = scan(node)
        if max_height < heightCurrent:
            max_height == heightCurrent

    return max_height


def main():
    # implement input form keyboard and from files

    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    n = int(input())
    # input values in one variable, separate with space, split these values in an array
    tree = int(input().split())
    treeElements = list(map(tree))
    # call the function and output it's result
    print(compute_height(n, treeElements))
    
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))