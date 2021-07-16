# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

def isrighttriangle(X1, Y1, X2, Y2, X3, Y3):
    A = (int(pow((X2 - X1), 2)) + int(pow((Y2 - Y1), 2)))
    B = (int(pow((X3 - X2), 2)) + int(pow((Y3 - Y2), 2)))
    C = (int(pow((X3 - X1), 2)) + int(pow((Y3 - Y1), 2)))
    
    if ((A > 0 and B > 0 and C > 0) and (A == (B + C) or B == (A + C) or C == (A + B))):
        return True
    else:
        return False