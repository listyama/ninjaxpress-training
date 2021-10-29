nama_buah = []
def tambah_nama_buah(nama):
    nama_buah.append(nama)
    print_nama_buah()

def print_nama_buah():
    for buah in nama_buah:
        print(buah)
    print("---")   

tambah_nama_buah("apel")
tambah_nama_buah("jeruk")
tambah_nama_buah("mangga")


#VERSI AWAL YG GA RINGKAS
# nama_buah.append("apel")
# for buah in nama_buah:
#         print(buah)
#         print("---")

# nama_buah.append("jeruk")
# for buah in nama_buah:
#         print(buah)
#         print("---")

# nama_buah.append("mangga")
# for buah in nama_buah:
#         print(buah)
#         print("---")
        
# nama_buah.append("pisang")
# for buah in nama_buah:
#         print(buah)
#         print("---")



