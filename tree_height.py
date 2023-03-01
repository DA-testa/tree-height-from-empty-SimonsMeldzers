# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    heightArr = [-1] * n

    def scan(node):
        if heightArr[node] != -1:
            return heightArr[node]
        if parents[node] == -1:
            heightArr[node] = 1
            return 1

        parentHeight = scan(parents[node])

        heightArr[node] = parentHeight + 1

        return heightArr[node]

    # Write this function
    max_height = 0
    for node in range(n):
        heightCurrent = scan(node)
        if max_height < heightCurrent:
            max_height = heightCurrent

    return max_height


def main():

    fileType = input()

    if "F" in fileType:
        fileName = input()
        if "a" in fileName:
            return
        if "test/" not in fileName:
            fileName = 'test/' + fileName
        if "test/" in fileName:
            with open(fileName) as f:
                n = int(f.readline().strip())
                parents = list(map(int, f.readline().strip().split()))
                height = compute_height(n, parents)
                print(height)
    elif fileType == "I":
        n = int(input())
        parents = list(map(int, input().split()))
        height = compute_height(n, parents)
        print(height)
    else:
        print('Error')
    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))