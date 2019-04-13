b = [[3,2,1], [3,2,4], [3,2,4], [1,1,1]]

matrix = len(b[0])
sementara = 0
hasil = []
for a in range(matrix):
    for x in b:
        sementara += x[a]
    hasil.append(sementara)
    sementara = 0

print(hasil)