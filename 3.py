
def hitungKembalian(total,uang):
    kembalian = uang - total

    #50.000
    while kembalian >= 50000:
        a1 = kembalian//50000
        print(a1,"x 50.000")
        kembalian -= a1*50000

    #20.000
    while kembalian >= 20000:
        a2 = kembalian//20000
        print(a2,"x 20.000")
        kembalian -= a2*20000

    #10.000
    while kembalian >= 10000:
        a3 = kembalian//10000
        print(a3,"x 10.000")
        kembalian -= a3*10000

    #5000
    while kembalian >= 5000:
        a4 = kembalian//5000
        print(a4,"x 5.000")
        kembalian -= a4*5000

    #2000
    while kembalian >= 2000:
        a5 = kembalian//2000
        print(a5,"x 2.000")
        kembalian -= a5*2000

    #1000
    while kembalian >= 1000:
        a6 = kembalian//1000
        print(a6,"x 1.000")
        kembalian -= a6*1000

    #500
    while kembalian >= 500:
        a7 = kembalian//500
        print(a7,"x 500")
        kembalian -= a7*500

#testing
total = 110500
uang = 200000

hitungKembalian(total,uang)
