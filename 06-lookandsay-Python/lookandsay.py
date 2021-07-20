# Write the function lookAndSay(a) that takes a list of numbers and returns a list of numbers
# that results from "reading off" the initial list using the look-and-say method, using tuples 
# for each (count, value) pair.
# 
# For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]


# def readArray():
#     a = []
#     l = int(input())
#     for i in range(l):
#         a.append(int(input()))
#     return a

def lookandsay(a):
    # your code goes here
    r = []
    #s = []
    j = 0
    count = 1
 
    if(len(a) == 0):
        return r
    for i in a:
        if(i!=j):
            r.append((count,j))
            j = i
            count = 1
        else:
            count = count + 1
    r.append((count,i))
    return r[1:]
