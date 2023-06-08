#global variables for parsing the data
master_array=[]
name=[]
list1=[]
list2=[]


#data tokenization
list0="""AAAAAAAAAAAAAAAAAAAAAAAA
1 NNNNNU NNNNNAAA NNNNN.NNNNNNNN +.NNNNNNNN +NNNNN-N +NNNNN-N N NNNNN
2 NNNNN NNN.NNNN NNN.NNNN NNNNNNN NNN.NNNN NNN.NNNN NN.NNNNNNNNNNNNNN""".split("\n")
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


list_org()
print(name)

def join_array():
    for i in name:
        master_array.append(i)

