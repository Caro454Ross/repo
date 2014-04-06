#DNA sequence

sequence = raw_input("Enter a series of nulceotide bases: ").upper()
if len(sequence)<6:
    print "WARNING: Sequence is shorter than 6 bases"
else:
    print "The first 3 bases are "+sequence[0:3]
    print "The last 3 bases are "+sequence[-3:]