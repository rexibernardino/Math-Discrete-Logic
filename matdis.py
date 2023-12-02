

import math

'''Ceiling and Floor'''
x = 7* 1.1428571428571428 + 4
# x = (12-4)/7
# x=math.sqrt(1)
ceil=math.ceil(1)
floor = math.floor(17)
print("ceil:",ceil)
print("floor: ",floor)
print (x)


'''recurrence relation '''

#x(n) = x(n-1)+2x(n-2), x(0) = 0 and x1 = 1

def x (n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return 8*x(n-1) - 16*x(n-2)
    # else: return (2**n  +1 )/ 3
    # # else : return -1*x(n-1) + 5
    # else: return 2* 3**n - (-1)**n

for i in range(0,2):
    print ("x",i,"=",x(i))

'''How many odd integers between  10000  and  99999  
(inclusive) whose digits are all different?
                COUNTING PROBLEM                '''

counter = 0 
for x in range(1000, 10000): 
	s = str(x) 
	if len(s) == len(set(s)) and x % 2 == 1: 
		counter += 1 
		# print(s) #kalau mau dipake utk nunjukin berapa banyak angkanya
print (counter)

'''PigeonHOLE diperumum'''
#Nilai indeks yang digunakan di Tel-U terdiri 
#atas: A, AB, B, BC, C, D, E, dan T. 
#Paling sedikit berapa banyak mahasiswa
#yang harus mengikuti suatu kuliah agar setidaknya ada
#orang yang memiliki nilai indeks yang sama?


#16 orang untuk indeks yang sama
N1 = 16-1
sum_sementara = (N1 * 8+1)-1
print("Nilai Indeks:",math.ceil(sum_sementara/8))


'''Rhesus'''
#Golongan darah manusia terdiri atas empat jenis, 
#yaitu: A, B, AB, dan O. Masing-masing golongan darah 
#memiliki dua jenis rhesus, yaitu + atau -. 
#Berapa banyak orang yang diperlukan untuk memastikan bahwa 
#di antara mereka setidaknya ada 5 orang dengan golongan 
#darah dan rhesus yang sama

#4*2 = 8 (untuk membedakan gol darah dan rhesus yg beda)
N2 = ((5-1)*8+1)-1 #5 untuk memastikan 5 orang yg berbeda
print("Rhesus:",math.ceil(N2/8))

'''IPK'''

#Indeks prestasi kumulatif (IPK) adalah bilangan desimal tiga
#digit berbentuk tidak kurang dari dan tidak lebih dari 0.00 
#dan tidak lebih dari 4.00.
#Berapa banyak minimal mahasiswa yang perlu dikumpulkan agar 
#setidaknya pasti ada 10 orang dengan IPK yang sama?

#4*10*10 =400 kemungkinan x (untuk angka ipk)
N3 = ((5-1)*401+1)-1

#banyak kemungkinan ipk yang berbeda adalah 401
print("IPK:",math.ceil(N3/401))

'''STRING BINER'''
#Berapa banyak string biner dengan panjang 5 yang diperlukan
#untuk memastikan bahwa terdapat 4 string biner yang sama?
#(String biner dengan panjang 5 contohnya 00000, 00001, 00010, dan 00011.)

#2**5 = 32 (untuk panjang biner 5)
N4 = ((3-1) *16+1)-1
print("Biner:",math.ceil(N4/32))