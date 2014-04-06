seq = raw_input("Enter a series of nulceotide bases: ")
rev=""
for i in range(1,len(seq)+1):
    rev=rev+seq[-i]
print "The reverse of "+seq+" is: "+rev