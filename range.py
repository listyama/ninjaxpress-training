# for i in range(3):
#     print(i)

# for i in range(1,3):
#     print(i)

# for i in range (1,20,2):
#     print(i)

# for i in range (2,10,2):
#     print(i)

#QUIZ
# nama = []
# list = []

# x = input("Jumlah orang: ")
# x = int(x)

# for n in range(x):
#     nama = input("Enter Name: ")
#     list.append(nama)
# print(list)

count = int(input("Berapa Data: "))

nama_pelanggan = []
umur_pelanggan = []

for i in range(count):
    print("Data ke {}". format(i+1))
    nama = input("Nama: ")
    umur = int(input("Umur: "))

    nama_pelanggan.append(nama)
    umur_pelanggan.append(umur)

for i in range(len(nama_pelanggan)):
    print("Pelanggan {} berusia {}". format(nama_pelanggan[i], umur_pelanggan[i]))
