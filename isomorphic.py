l=[7,9,1,69,89,4,30]
def sumsquare(l):
    odd=0
    even=0
    for i in l:
       if i%2==0:
         even = even + i**2
         odd = odd+i**2
    l=[odd,even]
    return(l)
print (sumsquare(l))
