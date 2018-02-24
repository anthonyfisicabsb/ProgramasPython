word='sodsncdzmxsjsjaqwarwadsteuiozxcavsderqiomlxnbcgfdv'
dictio=dict()

for chara in word:
    if chara not in dictio:
        dictio.__setitem__(chara,1)
    else:
        dictio.__setitem__(chara,dictio[chara]+1)
print(dictio)
