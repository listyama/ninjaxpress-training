#WHILE LOOP
# i = 1
# while i < 6:
#     print(i)
#     i+= 1

# print(i)

#CONTINUE -> ngeskip
# for i in range(5):
#     if i == 2:
#         continue #ini ibaratnya ngelongkap kalau ada 2 nya.
#     print(i)

# for i in range(10):
#     if i % 2 == 0: #apapun yg dibagi 2, modulus/sisa pembagiannya (%) = 0
#         continue
#     print(i)

#BREAK -> buat ngeberentiin iterasi
for i in range(5):
    if i == 2: #once ada ini, iterasinya akan berenti. gakayak continue yg ngeskip lalu lanjut
        break
    print(i)

