# -*- coding: utf-8 -*-
"""Untitled22.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GpxkU_vJcf7etIC-O4AjspYFfAh5CUsV
"""

#function
#

def greeting():
    print("Hello")

print("hii")

def greeting(username):
    print("Hello",username)

#argument/ formal argument/informal parameter
greeting("John")
greeting("emma")
greeting("raj")

def sumNo(a,b):
    print(a+b)

sumNo(10,20)

def sumNo(a,b):
    c=a+b
    print(c)
sumNo(10,20)
print(y)

def sumNo(a,b):
    c=a+b
    print(c)
    #function outside
a=10
y=20
sumNo(10,20)
print(y)

def sumNo():
    c=x+y
    print(c)
    #function outside
x=10
y=20
sumNo()

def fun():
    print("inside fun",x+10)

#yha se start
x=10
fun()
print(x)

x=10
x+10
print(x)

def fun():
  y=x+10
  print("inside fun",y)

#yha se start
x=10
fun()
print(y)

def fun():
    y=x+10
    print("inside fun",y)

#yha se start
x=10
fun()
print(y)

def fun():
    global x#bahar ki value add karne ke strat
    x=x+10
    print("inside fun",x)

#yha se start
x=10
fun()
print(x)

def ageAss():
    age=age+1
    print("inside fuc",age)

#yha se start
age=10
ageAss()
print(age)

def ageAdd():
    global age#variable jo bhi change karte h wo valriable m hoti h globle fuc se
    age=age+1
    print("inside fuc",age)

#yha se start
age=18
ageAdd()
print("outside function",age)

def ageAdd():
    global age#variable jo bhi change karte h wo valriable m hoti h globle fuc se
    age=age+1
    print("inside fuc",age)


age=18
ageAdd()
ageAdd()
ageAdd()
print("outside function",age)

def additionNo(num):
    print("num",id(num))
    print(num+10)

x=10
print("before function",id(x))
additionNo(x)

def additionNo(num):
    print("num",id(num))
    num=num+10
    print("new num" ,num)

x=10
print("before function",id(x))
additionNo(x)
print("After function of x:",id(x))

#know creat a fuction two value and both value devisibal by 2 other wise error
def

#*arg and *kwargs
def func(x):
    x=x+10
    print("x value in function:",x)


  #outside
num=10
func(num)
print("outside function",num)

#mutable data type
def func(mylist):
    print(mylist,type(mylist))
  #outside
list1=[10,20,30]
print("orignal:",list1,id(list1))
func(list1)
print("function call orignal:",list1,id(list1))

def func(mylist):
    mylist.append(60)
  #outside
list1=[10,20,30]
print("orignal:",list1,id(list1))
func(list1)
print("function call orignal:",list1,id(list1))

def func(mylist):
    print(mylist,type(mylist))
  #outside
list1=[10,20,30]
print("orignal:",list1,id(list1))
func(list1)

#lambda functions
#annymous function
#one line -inline
#
def square(x):
    return (x**2)
print(square(10))

#lambda parameter:expression
lambda x:x**2
#lambda ko kisi variable m hi save kar sakte h
out=lambda x:x**2
print(out(10))

#return keyword
def func(x):
    print(x+10)
#var=func
x=func(10)
print("return value:",x)

#return keyword
def func(x):
    return"hey"
#var=func()
x=func(10)
print("return value:",x)

#return keyword
def func(x):
    return"hey""hello"
    10/0
#var=func


x=func(10)
print("return value:",x)

#return keyword
def func(x):
    return["hey","hello"]

#var=func


x=func(10)
print("return value:",x)

x=func(10)
print(x)

func(10)

def func(s):
    total=0
    for i in s:
        total+=total
    return {s:total}

out=func