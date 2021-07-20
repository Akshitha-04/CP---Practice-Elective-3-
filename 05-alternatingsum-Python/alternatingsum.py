# Write the function alternatingSum(a) that takes a list of numbers and returns the 
# alternating sum (where the sign alternates from positive to negative or vice versa). 
# For example, alternatingSum([5,3,8,4]) returns 6 (that is, 5-3+8-4). If the list is empty, return 0.


# def readArray():
# 	a = []
# 	l = int(input())
# 	for i in range(l):
# 		a.append(int(input()))
# 	return a

def fun_alternatingsum(a): 
	sum1=0
	sum2=0
	if(len(a)==0):
		return 0
	for i in range(0,len(a),1):
		if(i%2 == 0):
			sum1 += a[i]
		else:
			sum2 += a[i]
	return sum1 - sum2



