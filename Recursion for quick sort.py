''' Create a program that use recursion to solve quick sort on a
given array'''

def aray(f,s,e):
    pos = s
    for i in range(s,e):
        if f[i]<f[e]:
            f[i],f[pos]=f[pos],f[i]
            pos+=1
        f[pos],f[e]=f[e],f[pos]
        return pos
def rec__qs(f,s,e):
    if s<e:
        pos = aray(f,s,e)
        rec__qs(f,s,pos-1)
        rec__qs(f,pos+1,e)

l=[3,45,1,2,34]
rec__qs(l,0,len(l)-1)
print(l)
