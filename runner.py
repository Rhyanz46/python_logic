import sys
from pathlib import Path

def main(argv):    
    filenya = Path(argv[0]).resolve()
    lines = open(filenya).read().split("\n")
    jumlah = len(lines)

    # a = [line.replace(' ', '') for line in lines[urutan]]
    # lines = [line.replace(' ', '') for line in lines]

    dump = []
    for urutan in range(len(lines)):
        a = lines[urutan].replace('\t','').split(' ')[0]
        dump.append({"no" : urutan, "data" : a[::-1]})

    # for urutan in range(len(lines)):
    #     a = lines[urutan].replace('\t','').split(' ')[0]
    #     for data in dump:
    #         aa = data['data']
    #         if a == "":
                # print("aaa")
                # print(str(urutan) + " " + aa)
            # if aa == a:
            #     print(data['no'])
    
    for data in dump:
        for urutan in range(len(lines)):
            # normal
            aa = lines[urutan].replace('\t','').split(' ')[0]
            if data['data'] == '':
                continue
            if data['data'] == aa:
                print(data['no'])
        # print(str(data['no']) + ' ' + data['data'])
                
    # for urutan in range(len(lines)):
    #     a = lines[urutan].replace('\t','')
    #     a = a.split(' ')
    #     if a[0] == 'cetak':
    #         print(a[1])

if __name__ == "__main__":
   main(sys.argv[1:])