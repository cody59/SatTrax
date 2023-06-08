#rules for parsing the data

Master_Dictionary={} #created to be able to pull any information from
name=[]
values=[]
#a is the name of the sattilite, b and c are lines one and two



#data tokenization
list0="""AAAAAAAAAAAAAAAAAAAAAAAA
1 NNNNNU NNNNNAAA NNNNN.NNNNNNNN +.NNNNNNNN +NNNNN-N +NNNNN-N N NNNNN
2 NNNNN NNN.NNNN NNN.NNNN NNNNNNN NNN.NNNN NNN.NNNN NN.NNNNNNNNNNNNNN""".split("\n")
list1=[]
list2=[]
def list_org():
    b=[]
    for i in list0:
        n=str(i).split()
        if n[0] == "1":
            list1.append(n)
        elif n[0] == "2":
            list2.append(n)
        if n[0] != "1":
            if n[0] != "2":
                name.append(n)
        else:
            "yay"#the code won't work without this >:(
def dic_org():
    for i in name:
        Master_Dictionary.update({i:[]})
    for i in list1:
        for n in Master_Dictionary:
           Master_Dictionary.update({n:[i]})
    for i in list1:
        for n in Master_Dictionary:
            Master_Dictionary.update({n:[i]})

list_org()
print(list2)