#Counts non-nucleotide bases
sequence = raw_input("Enter a series of nulceotide bases: ").upper()
count=0
for i in range(0,len(sequence)):
    if not (sequence[i] in 'ACTG'):
        count=count+1
        
print "The number of non-nucleotide bases = "+str(count)
