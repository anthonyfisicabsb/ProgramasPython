fhand=open('email.txt')
diasSemana=dict()

for linha in fhand:
    if linha.startswith('From'):
        linha=linha.split()
        if linha[2] not in diasSemana:
            diasSemana[linha[2]]=1
        else:
            diasSemana[linha[2]]+=1

print(diasSemana)
