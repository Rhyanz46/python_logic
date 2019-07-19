# def check(func):
#     def inside(a, b):
#         if a == b :
#             print("kalian tak boleh sama")
#             # return
#         func(a, b)
#     return inside


# @check
# def div(a, b):
#     print("hello div")
#     # return a


# print(div(10, 10)) # untuk menjalankannya
# del check #menghapus untuk sementara
# del div #menghapus untuk sementara
#-------------------------------------------------------

nama = ""

def detailcek():
    print("nama kau kosong")

def rulles(func):
    if nama == "":
        return detailcek # intinya dia harus nge-return sebuah fungsi
    else:
        return func

def app():
    print("hello guys")

app = rulles(app)

app() # untuk menjalankannya

del nama
del detailcek
del rulles
del app

# ---------------------------------------------------------


nama = "bagas"

def detailcek():
    print("nama kau bukan bagas")

def rulles(func, nama_input):
    if nama != nama_input:
        return detailcek # intinya dia harus nge-return sebuah fungsi
    else:
        return func

def app():
    print("hello guys")

app = rulles(app, "arian")

app() # untuk menjalankannya

del nama
del detailcek
del rulles
del app


# ---------------------------------------------------------


nama = "arian"

def rulles(func, nama_input):
    def detailcek():
        if nama != nama_input:
            print("kau bukan pemilik akun")
        return func
    return detailcek

def app():
    print("hello guys")

app = rulles(app, "messi")

app() # untuk menjalankannya

del nama
del rulles
del app

#---------------------------------------------------------- Dengan Parameter


nama = "karyawan"

def rulles(*argument):
    def cek(func):
        def detailcek():
            # if nama != nama_input:
            print("kau bukan admin")
            print(argument)
            return func()
            # return argument
        return detailcek
    return cek

@rulles(["admin", "ded"])
def app():
    print("hello guys")

app() # untuk menjalankannya

del nama
del rulles
del app
