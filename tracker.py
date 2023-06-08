#rules for parsing the data

Master_Dictionary={} #created to be able to pull any information from
name=[]
values=[]
#a is the name of the sattilite, b and c are lines one and two



#data tokenization
list="""AAAAAAAAAAAAAAAAAAAAAAAA
1 NNNNNU NNNNNAAA NNNNN.NNNNNNNN +.NNNNNNNN +NNNNN-N +NNNNN-N N NNNNN
2 NNNNN NNN.NNNN NNN.NNNN NNNNNNN NNN.NNNN NNN.NNNN NN.NNNNNNNNNNNNNN""".split("\n")
list1=[]
list2=[]

print(list)


for i in list:
    if i[0] == "1":
        list.append(i)
    elif i[0] == "2":
        list2.append(i)
    else:
        name.append(i)
print(list)

for i in name:
    Master_Dictionary.update({i:[]})
for i in list1:
    for n in Master_Dictionary:\
        Master_Dictionary.update({n:[i]})
for i in list1:
    for n in Master_Dictionary:\
        Master_Dictionary.update({n:[i]})

print(list)
