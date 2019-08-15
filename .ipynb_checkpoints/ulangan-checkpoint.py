a = 20
sementara = [0]
hasil = []

for i in range(a):
    for x in range(3):
        if x == 0:
            hasil.append(sementara[len(sementara) - 1])
        elif x == 1:            
            hasil.append(hasil[len(hasil) - 1]+i)
        elif x == 2:            
            hasil.append(hasil[len(hasil) - 1]+i)
            sementara.append(hasil[len(hasil) - 1]+i)

hasil.remove(hasil[0])    
print(hasil)