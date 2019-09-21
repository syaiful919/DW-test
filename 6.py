
def mrClints(operasi,n,index):

    if n <= 1000:
        list = []
        for i in range(0,n+1): 
            list.append(str(i))

        a = "".join(list)

        y = []
        for i in a:
            y.append(int(i)) 

        if operasi == "SUM":
            hasil = 0
            for i in index:
                hasil += y[i]
        if operasi == "MUL":
            hasil = 1
            for i in index:
                hasil *= y[i]
        if operasi == "SUB":
            hasil = 10
            for i in index:
                hasil -= y[i]
            hasil -= 10
        if operasi == "DIV":
            hasil = 10
            for i in index:
                hasil /= y[i]
            hasil *= 10

    else:
        print("N terlalu besar")

    print(hasil) 


#Testing
n = 20
index = [11,13,15]
operasi = "SUM"

mrClints(operasi,n,index)
