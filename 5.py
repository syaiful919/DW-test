
def buyEggs(tanggal,uang):
    telur = uang//2500
    kembalian = uang % 2500

    #membuat list bilangan prima
    prima = []
    for mungkinPrima in range(2, 32): 
        adalahPrima = True
        for angka in range(2, mungkinPrima):
            if mungkinPrima % angka == 0:
                adalahPrima = False
                break 
        if adalahPrima:
            prima.append(mungkinPrima)
    
    #syarat bonus berdasar tanggal
    if tanggal in prima:
        bonus = 2
        if (tanggal % 5) == 0:
            bonus *= 10

    elif (tanggal % 2) != 0:  
        bonus = 3
        if (tanggal % 5) == 0:
            bonus *= 5

    #syarat minimal 1 lusin baru mendapat bonus
    n = telur//12
    
    if telur < 12:
        bonus *= 0
    else:
        bonus *= n
    
    print("anda membeli", telur, "telur")
    
    #jika mendapat bonus
    if bonus > 0:
        print("bonus telur untuk",n,"lusin telur =",bonus)
        telur += bonus
        print("telur + bonus =",telur)
    
    #jika ada kembalian
    if kembalian != 0:
        print("kembalian =",kembalian)
        

#testing
uang = 60000
tanggal = 13

buyEggs(tanggal,uang)
