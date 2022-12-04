'''COP = int(input("COP="))
CGST = int(input("CGST="))
SGST = int(input("SGST="))
amount=(CGST/100)*COP
amount=(SGST/100)*COP
totalcost=(COP+CGST+SGST)
print(totalcost)'''

# a=list(input("list item"))
# list = ("apple", "mango", "cherry")
# print(list[:2])


# num=int(input("num:"))
# if num%2==0:
#     print("pn")
#
# elif num%3==0:
#     print("not pn")
#
# elif num%5==0:
#     print("not pn")
# else:
#     print("num")

# num = int(input())
# x = num
# for i in range(2, num):
#     if num % i == 0:
#         flag = 0
#         break
#     else:
#         flag = 1
# if flag == 1:
#     print("prime")
# else:
#     print("no")

# n=str(input("str: "))

# for i in n:
#     if i==" ":
#         continue
#     print(i, end="")
#

# sum of numbers from 1 to 25, 50 to 75, 90 to 100
# def sum(x,y):
#     s = 0;
#     for i in range(x,y+1):
#         s=s+i;
#     print(s)
# sum(1,25)
# sum(50,75)
# sum(90,100)

# p = 20  # global variable
# def sum():
#     q = 10  # local variable
#     print("the value of q", q)
#     print("the value of p", p)
# sum()
# print("the value of p", p)
#
# p = 20  # global variable
# def sum():
#     q = 10  # local variable
#     print("the value of q", q)
#     print("the value of p", p)
# sum()
# print("the value of p", p)

# parameter with default values
# def msg(name ,mesage="welcome to LPU"):
#     print("hello",name, mesage)
# msg("harry")

# keyword arguments
# def msg(name, age):
#     print("name=",name, "age=",age)
# msg(age=25, name="harry")

# postitional argument
# def msg(name, age):
#     print("name=",name, "age=",age)
# msg("harry")

# s=10
# def call():
#     f = (s+p)**p
#     print(f)
#     print(p)
#
# p=int(input("p:"))
# call()


# h1="Hello"
# h2="Hello"
# print(id(h1))
# print(id(h2))
# value is changing because memory location is changing

# a=str("hello python")
# b=str("i love")
# c=a[5:12]
# d=b[0:6]
# e=d+c
# print(e)

# comparison of string
# s1="ABC"
# s2="abc"
# print(s1>s2)
# print(s1<s2)
# print(s1==s2)

# format method
# a='{}plus{}equal{}'.format(4,5,'9')
# print(a)


# testing string
# string is alphabet, alphanumeric, digit
# s="python programing"
# print(s.isalpha())
# print(s.isalnum())
# print(s.isdigit())


# searching string
# s: str = "python programming"
# print(s.endswith("n"))
# print(s.startswith("python"))
# print(s.find("k"))
# print(s.count("o"))
# print(s.rfind("g"))

# string conversion
# capitalize, lower, upper
# s="python programming"
# print(s.capitalize())
# print(s.lower())
# print(s.upper())
# print(s.title())
# print(s.swapcase())
# print(s.replace("python", "what is"))


# stripping unwanted character
# s="python programming"
# print(s.lstrip("python"))
# print(s.rstrip("programming"))
# print(s.lstrip("/t"))

# justific / formatting
#  center left right
# s="Hello World"
# print(s.center(50))
# print(s.ljust(10))
# print(s.rjust(20))

# def countB(hello):
#     count=0
#     for i in hello:
#         if (i==i):
#             count=count+1
#     return count

# s="python programming"
# print(s.upper())

# s=input("x: ")
# a="aeiouAEIOU"
# for i in s:
#     if i in a:
#         print(i)
#     else:
#         print("")

# list
# l1=["a","b","c","d"]
# l2=[1,2,3,4]
# print(l1+l2)
# l3=l1*2
# print(l3)

# list comprehension
# list=[1,2,3,4,]
# l1=[]
# l2=[]
# for i in range (list):
#     if i%2==0:
#         l1.append()
#         print(l1)
#     else:
#         l2.append()
# print("list",l1)
# print("even",l2)

# list1=["a","b","c","d","e","f"]
# list1.insert(3,"d")
# print(list1)
#
# list1.pop(3)
# print(list1)
#
# list1.remove("e")
# print(list1)
#
# list1.sort()
# print(list1)
#
# list1.reverse()
# print(list1)
#
# list1.append("a")
# print(list1)
#
# list1.extend("g")
# print(list1)

# s=("welcome to python")
# print(s.split())
#
# def item(list)
#     list=[,2,3,4,]
#     for i in list:

# class college:
#     def student(self):
#         self.name = input("shudhanshu")
#         self.rollno = input("04")
#         self.section = input("k22er")
#     def display(self):
#         print("name", self.name)
#         print("rollno", self.rollno)
#         print("section", self.section)
# a=college()
# a.student()
# a.display()

# class booking:
#     def hotel(data):
#         data.name=input("Name: ")
#         data.stay=input("stay: ")
#         data.fooding=input("fooding: ")
#     def display(data):
#         print("Nmae", data.name)
#
#         print("stay",data.stay)
#         print("fooding",data.fooding)
# a=booking()
# a.hotel()

# class college:
#     def __init__(course, name, age):
#             course.name=name
#             course.age=age
# a=college("hena", "28")
# print(a.name)
# print(a.age)

# class college:
#     def __init__(self, name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"{self.name} {self.age}"
# a=college("hena","29")
# print(a.name)
# print(a.age)

#     def add(self):
#         print("My name is: " + self.name)
# a=college("hena","16")
# a.add()

# class school:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(self.name, self.age)
# class std(school):
#     def __init__(self,name,age):
#         school.__init__(self,name,age)
# x=std("hena",17)
# x.display()


    # pass

# x=std("hena","12")
# x.display()

# class A:
#     pass
# class B:
#     pass
# class C:
#     pass
# i=A()
# j=B()
# k=C()
# print(isinstance(i,A))
# print(isinstance(j,B))
# print(isinstance(k,C))

# method overloading
# class maths:
#     def add(a, b):
#         print(a, b)
#     def add(c, d, a, b):
#         print(c, d, a, b)
# p=maths()
# p.add(10,20)

# class A:
#     print("i am class A")
#
# class B(A):
#     print("i am class B")
#
# p=A()
#
#  font times new roman 12 jsutify alignmant

# dictonary

# m={"a:1", "b:2", "c:3", "d:4", "e:5"}
# a=[]
# b={}
# for key,val in m.items():
#     if val not in a:
#         a.append(val)
#         b[key]=val
# print(str(b))

# dict1={"A","B","C","D","A","D"}
# d={frozenset(item.items()):item for item in dict1}
# values()
# print(z)

# x=int(input())
# y=int(input())
# z=int(input())
# a=[[b,c,d] for b in range(x+1) for c in range(y+1)
# for d in range(z+1)
#    if (x+y+z!=3)]
# print(a)

d1=input()
d2=input()
dict3={d1[i]:d2[i] for i in range(len(d1))}
print(dict3)