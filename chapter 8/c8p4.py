'''
sum(1)=1
sum(2)=1+2
sum(3)=1+2+3
sum(n)=1+2+3+4........ n

sum(n)= sum(n-1)+n

'''
c=int(input("enter you recursion number "))
def sum(n):
    if(n==1):
        return 1 #ye na karte to n ki value sum (0) sum of (-1) pr jane lagega 
    return sum(n-1)+n

print(sum(c)) 