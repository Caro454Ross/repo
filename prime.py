number = int(raw_input("Enter a number: "))
factors = range(2,number)

prime= 1
for i in range(0,len(factors)):
    if number%factors[i]==0:
        prime=0

if prime:
    print str(number)+ " is a prime number"
else:
    print str(number)+ " is not a prime number"
    