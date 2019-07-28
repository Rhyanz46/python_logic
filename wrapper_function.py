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

# ---------------------------------------------------------


nama = "arian"

def rulles(func):
    def detailcek():
        if nama != "a":
            print("kau bukan pemilik akun v2")
            return
        return func()
    return detailcek

@rulles
def app():
    print("hello guys")


app() # untuk menjalankannya

del nama
del rulles
del app


#---------------------------------------------------------- Dengan Parameter

def rulles(*argument):
    def cek(func):
        def func_anak():
            for a in argument:
                print(a)
            return func()
            # return argument
        return func_anak
    return cek

@rulles("admin" , "ded", "ded")
def app():
    print("hello guys")

app() # untuk menjalankannya

del rulles
del app


########################### belajar functools ###########################


nama = "arian"

def rulles():
    def cek(func):
        if nama == "arian":
            return func
        else:
            def wrong():
                print("kau bukan arian")
            return wrong
    return cek

@rulles() # callable
def app():

    """saya adalah documentation"""
    
    data = 'ini adalah nilai dari sebuah function yang bernama "app"'
    print("hello arian")

app()
print(app.__doc__)  #bisa membaca atribut => karena dia callable
del app
del rulles
del nama



from functools import wraps


nama = "arian"

def rulles(func):
    def cek():
        if nama == "arian":
            return func()
        return
    return cek

@rulles # not callable
def app():

    """saya adalah documentation"""

    data = 'ini adalah nilai dari sebuah function yang bernama "app"'
    print("hai arian")

app()
print(app.__doc__) #tidak bisa membaca atribut => karena tidak callable maka di perlukan wraps function dari functools
del app
del nama



nama = "arian"

def rulles(func):

    @wraps(func) # di modifikasi menjadi callable
    def cek():
        if nama == "arian":
            return func()
        return
    return cek

@rulles # not callable
def app():

    """saya adalah documentation"""

    data = 'ini adalah nilai dari sebuah function yang bernama "app"'
    print("haaaii arian")

app()
print(app.__doc__) #tidak bisa membaca atribut => karena tidak callable maka di perlukan wraps function dari functools
del app
del nama