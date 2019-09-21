
def drawline(kata):
    y = []
    for i in kata:
        y.append(i)

    j = 0
    for i in y: 
        print(" "*j + i)
        j += 3 

#testing
kata = "DUMBWAYS"

drawline(kata)
