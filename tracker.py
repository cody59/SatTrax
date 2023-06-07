#rules for parsing the data

Master_Dictionary={a:[b,c]} #created to be able to pull any information from
#a is the name of the sattilite, b and see are lines one and two



#data tokenization
list=["""AAAAAAAAAAAAAAAAAAAAAAAA
1 NNNNNU NNNNNAAA NNNNN.NNNNNNNN +.NNNNNNNN +NNNNN-N +NNNNN-N N NNNNN
2 NNNNN NNN.NNNN NNN.NNNN NNNNNNN NNN.NNNN NNN.NNNN NN.NNNNNNNNNNNNNN"""]

for i in list:
    for n in range(len(i)):
        if i[0] == "1":
            holder=i.split()
            
        elif i[0] == "2":
            
        else:
            print(str(i))