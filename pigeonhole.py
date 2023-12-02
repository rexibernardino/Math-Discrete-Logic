import math
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