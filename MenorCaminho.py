from math import sqrt

def distancia(obj, obj2):
    retorno = (obj[0]-obj2[0])**2 + (obj[1]-obj2[1])**2

    return sqrt(retorno)

arquivo = open('dados-008.dat', 'r')

lista_particula = list()

for line in arquivo:
    string = line.split('\t')
    lista_particula.append([float(string[0]), float(string[1])])

caminho = list()
dist_tot = 999999999.999999
for part in lista_particula:
    caminho_aux = [part]
    dist_tot_aux = 0.0
    while len(caminho_aux) < len(lista_particula):
        dist_aux = 99999999999999999999999.999
        obj_aux = None
        for obj in lista_particula:
            if obj not in caminho_aux and distancia(obj, caminho_aux[-1]) < dist_aux:
                dist_aux = distancia(obj, caminho_aux[-1])
                obj_aux = obj

        caminho_aux.append(obj_aux)
        dist_tot_aux += dist_aux

    if dist_tot_aux < dist_tot:
        dist_tot = dist_tot_aux
        caminho = caminho_aux

for part in caminho:
    print(part[0], part[1])

print(' ')
print('Distancia total: ', dist_tot)
