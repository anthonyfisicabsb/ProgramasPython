string='shxncvbqetanjssbsçdbhskdoahsoehascnvcvcciiuwyyatsbxam'
dictio=dict()

for linha in string:
    dictio[linha]=dictio.get(linha,0)+1

print(dictio)
