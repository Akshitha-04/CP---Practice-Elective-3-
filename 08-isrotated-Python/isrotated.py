# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.


def rotateRight(s):
    r = s[0:len(s)-1]+s[len(s)-1]
    return r

def isrotated(str1, str2):
    n=len(str1)
    str1=str1
    for j in range(-1,n):
        str1=str1[j:] + str1[:j]
        if(rotateRight(str1) == str2):
            return True
    return False

