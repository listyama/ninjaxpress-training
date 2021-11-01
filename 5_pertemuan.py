# #MODULES
# import mymodule

# mymodule.greeting("Listya")


# #MATH MODULES
# import math #-> nanti disini bisa ada formula lainnya
# import datetime

# x = math.pi
# print(x)

# x = math.sqrt(64)
# print(x)

# print(datetime.datetime.now())

###
#FILE HANDLING
###

# f = open("file.txt", "a")
# f.write("Added text.")
# f.close()

f = open("file.txt", "a")
f.write("Added text\n") #->sama kayak yg atas tapi ini ngebuat jadi keenter
f.close()


f = open("file.txt", "a")
f.write("Hello!\n")
f.close()

###
#FILE HANDLING - READ
###
f = open("file.txt", "r")
print(f.read())

f = open("file.txt", "r")
print(f.read(5))

f = open("file.txt", "r")
print(f.readline())

# import os

# os.remove("file.txt") #ini untuk ngapus

###
###QUIZZZ
###

pi = 22/7
def luas_persegi (sisi):


