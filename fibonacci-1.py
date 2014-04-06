#Computes the sum of the multiples of 5 terms of fibonacci sequence

terms = [1,2]
index=1
while (terms[index]+terms[index-1])<=4000:
    next_term=terms[index]+terms[index-1]
    terms.append(next_term)
    index=index+1
    
sum_multiple5=0
for i in range(0,len(terms)):
    if terms[i]%5==0:
        sum_multiple5=sum_multiple5+terms[i]
    
print terms
print ("The sum of all multiples of 5 within fibonacci up to 4000 is : ")+str(sum_multiple5)
