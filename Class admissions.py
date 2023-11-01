class Admission:
    def __init__(self,ne,fn,s,r,de,fd,tt):
        self.ne = ne
        self.fn = fn
        self.s = s
        self.r = r
        self.de = de
        self.fd = fd
        self.tt = tt
    def print(self):
        print("NAME:",self.ne)
        print("FATHER NAME:",self.fn)
        print("SEAT NO:",self.s)
        print("ROLL NO:",self.r)
        print("DEPARTMENT:",self.de)
        print("FIELD:",self.fd)
        print("TEST:",self.tt)

n = int(input("How many student you want to Enroll?:"))
for i in range(n):
    print("Enter Details")

N = str(input("Enter Name:"))
f_n = str(input("ENTER FATHER NAME:"))
s_no = str(input("ENTER SEAT NUMBER:"))
r_no = int(input("ENTER ROLL NO:"))
d = str(input("ENTER DEPARTMENT NAME:"))
f = str(input("ENTER FIELD:"))
t_sc = int(input("ENTER TEST SCORE:"))

z = Admission(N,f_n,s_no,r_no,d,f,t_sc)
print(z.print())
input()
