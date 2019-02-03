import sys
from pathlib import Path

def main(argv):    
    try:
        filenya = Path(argv[0]).resolve()
        lines = open(filenya).read().split("\n")
        vocal = ['a', 'i', 'u', 'e', 'o']
        kata = lines
        jumlah = len(lines)
        index_vocal = []
        jumlah_benar = []
        konsonan_lebih3 = []
        output = []
        checked = []

        # print(jumlah)
        # for i in lines:
        #     print(i)

        for i in range(len(kata)):
            nn = 0
            n = 0
            v = 0
            k = 0
            for x in kata[i]:
                if x in vocal:
                    n=0
                    v+=1
                    jumlah_benar.append(n)
                    if i in index_vocal:
                        continue
                    index_vocal.append(i)
                    index_vocal = list(set(index_vocal))
                else:
                    n+=1
                    k+=1
                    jumlah_benar.append(n)

                    if i in checked:
                        continue
                    if n >= 3:
                        output.append("sulit") 
                        checked.append(i)
                        checked = list(set(checked))
            
            if i in checked:
                continue
            if k > v:
                output.append("sulit")
            else:
                output.append("gampang")
            checked.append(i)
            checked = list(set(checked))

        # print("")
        for a in output:
            print(a)
    except:
        print("")
        print("Ada kesalahan ...")
        print("Coba ulangi :)")

if __name__ == "__main__":
   main(sys.argv[1:])