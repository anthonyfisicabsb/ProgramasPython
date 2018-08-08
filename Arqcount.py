filename=input('Enter file name: ')
aux=True
count=0
tot=0.0
while aux:
	try:
		novoarquivo=open(filename)
		aux=False
	except:
		print('Nome de arquivo não encontrado!')
		filename=input('Enter file name: ')
for linhas in novoarquivo:
	if linhas.startswith('X-DSPAM-Confidence:'):
		pos=linhas.find(':')
		count+=1
		tot+=float(linhas[pos+1:])

if count>0:
	print('Encontrou-se %d linhas' % count)
	print('A média é',tot/count)
else:	
	print('Encontrou-se 0 linhas e a média foi 0')