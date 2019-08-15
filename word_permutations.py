# analisa : 

# ada suatu kata, kemudian buat semua permutasi dari kata tersebut

# disini misalnya kita punya kata="itak" kata kata yang akan terbuat salahsatunya adalah "kita"
# :
# 'itak', 'itka', 'iatk', 'iakt', 'ikta', 'ikat', 'tiak', 'tika', 'taik', 'taki', 'tkia', 'tkai'
# 'aitk', 'aikt', 'atik', 'atki', 'akit', 'akti', 'kita', 'kiat', 'ktia', 'ktai', 'kait', 'kati'

# mari kita a   nalisa :
# misalnya ada dua huruf misalnya "au" maka ankan terbentuk:
# 'au', 'ua'




Perm(kata):
    if len(kata) <= 1:
        return [kata]
    hasil = []
    for a in range(len(kata)):


# https://docs.python.org/3/reference/lexical_analysis.html