fname=input('Digite o nome do arquivo: ')
try:
    fhand=open(fname)
except:
    print('Arquivo não pôde ser aberto: ',fname)
    exit()
counts=dict()
for line in fhand:
    line=line.strip()
    line=line.lower()
    words=line.split()
    for word in words:
        if word not in counts:
            counts.__setitem__(word,1)
        else:
            counts.__setitem__(word,counts[word]+1)
print(counts)
