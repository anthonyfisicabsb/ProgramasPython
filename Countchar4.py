import string

fname=input('Digite o nome do arquivo: ')
try:
    fhand=open(fname)
except:
    print('Arquivo não pôde ser aberto: ',fname)
    exit()

counts=dict()
for line in fhand:
    line= line.strip('a')
    line=line.lower()
    line=line.strip()
    words=line.split()
    for word in words:
        if word not in counts:
            counts[word]=1
        else:
            counts[word]+=1

print(counts)
