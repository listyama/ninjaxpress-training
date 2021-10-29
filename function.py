#Contoh 1
# def myfunction():
#     print("Hello from a function")

# myfunction() #->cara manggil dan jalanin print function di atas

#Contoh 2 (FUNCTION PARAMETER) -> Udah diisi nilainya sbg nama
# def myfunction(nama, umur):
#     print("Hello {} {}".format(nama, umur))
    
# myfunction("listya",21)

#Contoh 3 (DEFAULT PARAMETER)
def myfunction(nama, umur=""): #->"" ini menandakan function yg gaada umur utk ttp ke run dengan blank. tp kl didefine, bakal ngikut ini
    print("Hello {} {}".format(nama, umur))
    
myfunction("listya")
myfunction("azura", 21)