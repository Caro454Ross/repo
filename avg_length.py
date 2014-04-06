#Calculates Average length of DNA sequences

sequence = raw_input("Enter a series of nulceotide bases [blank line to stop]: ")
count=0
length=0
while sequence!="":
    count=count+1
    length = length+len(sequence)
    sequence = raw_input("Enter a series of nulceotide bases [blank line to stop]: ")
print "The avergage length of the sequences is: "+str(length/count)
    
