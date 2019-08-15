class Orang:
    nama = "arian"
    umur = 12

orang = Orang()

#biasa
print("ambil nilai atribut biasa \t : {}".format(orang.nama))
# dinamic
print("ambil atribut dengan dinamis \t : {}".format(getattr(orang, 'nama')))
## cek
print("cek atribut dengan dinamis \t : {}".format(hasattr(orang, 'nama')))
# coba juga
# .
# setattr
# delattr