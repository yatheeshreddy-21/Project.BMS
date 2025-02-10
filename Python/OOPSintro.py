# # To ACCESS/MODIFY
# class School:
#     sname = "Christu"
#     sloc = "SMP"

# print(School.sname)
# s1 = School
# print(s1.sname)
# print(s1.sloc)

# School.sname="Vignan"
# School.sloc="Penukonda"
# print(s1.sname)
# print(s1.sloc)


# # # Type of Members -- Class Members, Object Members
# class Bank:
#     bname="SBI"
#     bloc="PKD"
#     bifsc="SBIN007"

# c1=Bank()
# c2=Bank()

# c1.cname="Yatheesh Reddy"
# c1.phno=6309808037
# c1.accno=284569071122

# c2.cname="Devansh Reddy"
# c2.phno=6309808037
# c2.accno=784569072211

# print(c1.bname)
# print(c1.bloc)
# print(c1.bifsc)
# print(c1.cname)
# print(c1.phno)
# print(c1.accno)

# print(c2.bname)
# print(c2.bloc)
# print(c2.bifsc)
# print(c2.cname)
# print(c2.phno)
# print(c2.accno)


# # Constructer _____/ __init__Method / 
# class Bank:
#     bname="SBI"
#     bloc="PKD"
#     bifsc="SBIN007"

#     def __init__(self,cname,phno,accno):
#         self.cname=cname
#         self.phno=phno
#         self.accno=accno

# c1=Bank("Yatheesh Reddy",6309808037,12345688)
# c2=Bank("Devansh Reddy",6309797870,227378438)
# Bank.bname = "SMP"
# print(c1.bname)
# print(c1.bloc)
# print(c1.bifsc)
# print(c1.cname)
# print(c1.phno)
# print(c1.accno)
# print(c2.bname)

### Type of Methods (object,class,static)____________1_object
# class Bank:
#     bname="SBI"
#     bloc="PKD"
#     bifsc="SBIN007"

#     def __init__(self,cname,phno,accno):
#         self.cname=cname
#         self.phno=phno
#         self.accno=accno
    
#     @classmethod
#     def display(cls):
#         print(cls.bname,cls.bloc,cls.bifsc)
    
#     @classmethod
#     def ch_bname(cls,new):
#         cls.bname=new

# c1=Bank("Yatheesh Reddy",6309808037,123456778)

# #c1.display()
# Bank.display()
# Bank.ch_bname("canara")
# Bank.display()
# #c1.ch_phno(7893393201)
# #c1.display()
# 
# 


# ######Constructor chaining ####
# class A:
#     a=10
#     b=22

#     def __init__(self,c,d,e,f,h):
#         self.c=c
#         self.d=d
#         self.e=e
#         self.f=f
#         self.h=h 

# class B(A):
#     i=20

#     def __init__(self,c,d,e,f,h,j,k):
#         super().__init__(c,d,e,f,h)
#         self.j=j
#         self.k=k 
#     def disp(self):
#         print(y.a,y.b,y.c,y.d,y.e,y.f,y.h,y.i,y.j,y.k)
# y=B(2,3,4,5,6,7,8)

# y.disp()


class A:
    a=10
    b=20

    def __init__(self,c,d):
        self.c=c
        self.d=d

class B:
    a=50
    n=60

class C:
    a=70
    q=80


class D(C,B,A):
    x=90
    y=100

ob1=D(30,40)
print(ob1.a)

