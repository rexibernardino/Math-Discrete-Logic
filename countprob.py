'''How many odd integers between  10000  and  99999  
(inclusive) whose digits are all different?
                COUNTING PROBLEM                '''
import math

counter = 0 
for x in range(2000, 3000): 
	# s = str(x) 
	# if len(s) == len(set(s)) and x % 2 == 1: 
		counter += 1 
		# print(s) #kalau mau dipake utk nunjukin berapa banyak angkanya
print (counter)


# print(math.count())