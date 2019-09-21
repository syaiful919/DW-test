import random
import string


def sn(n):
    x = string.ascii_letters + string.digits   
    hasil = []
    for i in range(n):
        y = []
        for j in range(4):
            z = "".join(random.choice(x) for k in range(4))
            y.append(z)
        hasil.append(y[0]+"-"+y[1]+"-"+y[2]+"-"+y[3])
    for l in range(len(hasil)): 
        print(hasil[l])

#testing 
n = 250

sn(n)
