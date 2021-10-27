#NESTED LOOP -> looping dalam looping
#CONTOH 1
# for i in range(3): #i itu adalah 0,1,2.
#     print('i = {}'. format(i))
#     for j in range(3): #j itu adalah 0,1,2.
#         print('j: {}'. format(j))

#hasilnya bakal setiap i = 0, bakal j=0, j=1, j=2

#CONTOH 2
# for baris in range(5):
#     for kolom in range(5):
#         print('{}.{}'. format(baris+1, kolom+1), end=' ')
#         #end ini fungsinya utk ga dienter jd hanya spasi
#     print()

#QUIZ
x = [1,2,3,4,5]
y = [2,4,3,5,6]
z = 0

for i in x:
    for j in y:
        if i==j:
            z=z+1
print(z)