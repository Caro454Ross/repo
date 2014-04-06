seq = raw_input("Enter a series of nulceotide bases: ")
rev=""
for i in range(1,len(seq)+1):
    if seq[-i]=="t" or seq[-i]=="T" :
        rev=rev+"U"
    else:
        rev=rev+seq[-i]
        
print "The reverse of "+seq+" is: "+rev