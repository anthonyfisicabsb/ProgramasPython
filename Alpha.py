counts={'chuck':1,'annie':42,'jan':100}
lst=[]
for kkey in counts:
    lst.append(kkey)
print(lst)
lst.sort()
for key in lst:
    print(key,counts[key])
