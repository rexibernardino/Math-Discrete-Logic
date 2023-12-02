import math
counter = 0 
for x in range(1, 126): 
	s = str(x) 
	if x%7==0 or x % 3 == 0 or x%5==0 : 
		counter += 1 
		# print(s) #kalau mau dipake utk nunjukin berapa banyak angkanya
print (counter)

print(math.factorial(7)/math.factorial(2))


# a1 = 4
# b1 = 2
# print((2*a1) + b1)

# r =2,4,6,8
# d =1,2,3,4