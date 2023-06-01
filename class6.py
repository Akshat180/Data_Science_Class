# join method 

s ='hello'
ls = list(s)
print(ls)

s2=''.join(ls)
print(s2)

s3=':'.join(ls)
print(s3)

# shortend 
def eo(n):
    return'even'if n%2 == 0 else 'odd'
print(eo(2))

# lambda
eo= lambda n:'even'if n%2 == 0 else 'odd'   # doing this code using lambda
print(eo(2))

# map 
l=list('1234')
l2=list(map(int,l))
print(l2)

#example

# n=[22,55,10,86,4]
# l2 = lambda m : 'even' if (lambda n : (n**2)+1)(m)%2==0 else 'odd'

# m=list(map(l2,n))
# print(m)

# modules


