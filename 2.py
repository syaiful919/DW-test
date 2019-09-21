
def check(kata,kalimat):
    for n in kata:
        if n in kalimat:
            print("true")
        else: 
            print("false")

#testing           
datakey = ["dumb","ways","the","best"]
word = "dumbways"

check(datakey,word)
