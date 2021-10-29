#DICTIONARY
pelanggan = {
    "nama" : "listya",
    "umur" : 21
}

pelanggan_2 = {
     "nama" : "zura",
     "umur" : 19
}

#kalau seandainya ada beberapa pelanggan, bisa pakai for loop.
# for x in pelanggan:
#     print(x) #-> nama
#     print(pelanggan[x]) #-> namanya (print nama pelanggan)
#     print(pelanggan_2[])

#PRINT SATU2
# # print (pelanggan["nama"])
# print ("Nama = {}". format (pelanggan["nama"]))
# print ("Umur = {}". format (pelanggan["umur"]))

# #bisa diubah nilai 21 yg sebelumnya, dan dimunculin di format baru
# pelanggan ["umur"] = 22
# print ("Umur baru = {}". format (pelanggan["umur"]))

#BIKIN LIST DICTIONARY
# daftar_pelanggan = []
# daftar_pelanggan.append(pelanggan)
# daftar_pelanggan.append(pelanggan_2)

# for pelanggan in daftar_pelanggan:
#     print("Nama = {}".format(pelanggan["nama"]))
#     print("Umur = {}".format(pelanggan["umur"]))

#QUIZZZZ
mydict = {
    'Name':'Zara', 
    'Age':7, 
    'Class':'First'
    }

mydict['Age'] = 8
mydict['School'] = 'DPS School'

print("dict['Age']: ", mydict['Age'])
print("dict['School']: ", mydict['School'])

#-> awalnya gaada key School, tp di print ada sehingga 
# dia jadi nambahin index baru dan data baru si school tsb
