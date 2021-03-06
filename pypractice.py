

# let's play with string in python
# s1 = 'abcd efghij'
# print (s1.split('c'))

# string formatting
# x = "sometjonf here: {}".format("insert me")
# print (x)
#
# x = "sometjonf here: {} item two: {}".format("insert me1", "two2")
# print (x)
#
# x = "item1: {x} item2:{y}".format(x="dog", y="cat")
# print (x)

# ls = [1,1,1,1,'df','gh',True]
# # print(ls[::-1])
# ls.sort()
# print(ls)


# nested list --
#ls = [1, 3, 4, [x, y, z]] #give an error bcz x is not an variable here so...

# ls = [1,2,3,['x','y','z']]
#
# print(ls[3][1])



# Matrix
#list comprehession

# m = [[1,2,3],[4,5,6],[7,8,9]]
#
# # first_col = [ row[0] for row in m ]
# #print(first_col)
# sec_row = [ col[1] for col in m ]
#
# print (sec_row)



# # Dictionary
# d = {"k1": 123, 'k2': 'value', 'k3': {'ki':[1, 2, 3]}}
# print (d['k3']['ki

# #Tuples
# unordered, unique elements
# t = (1,2,3)
# print t
# tuple are immutable, so we can't change the value of tuple
# t[1] = 5 will throw an error

# # Sets
# unordered, unique elements
# x = set()
# x.add(1)
# x.add(2)
# # add duplicate elements, but set will ignore them
# x.add(2)
# print x
# convert list into set
# setList = set([1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3])
# print setList

#Assignment Ques
#get 'Hello' from below Dictionary

# d = {'k1':[{'k2':['k3',['hello']]}]}
# re = d['k1'][0]['k2'][1][0]
# print re


# # Functions
# # def
#
# # 'filter' Functions
# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # can be replaced by lamda function
# def even_bool(num):
#     return num%2 == 0
#
# # lamba expression
# evens = filter(lambda num: num%2 == 0, ls)
#
# # filter
# #evens = filter(even_bool, ls) #takes 2 args first is functios and sec list/tuple/string

#print evens

# Python Functions
# st = "Love Cricket! #I'm a fast bowler"
# # re = split() # by default split by space
# # re = st.split('#')
# # accessing 1st element
# result = st.split('#')[1]
# print result
#
# # 'in' operator
# print ('x' in [1,2,3]) # result would be False
# print ('x' in [1,2,3,'x']) # result would be True

# return True if seq. of no. 1,2,3

# def arrCheck(arr):
#     for i in range(len(arr)-2):
#         if arr[i] ==1 and arr[i+1] ==2 and arr[i+2] == 3:
#             return True
#     return False

# Python Level Two
# Scope
# LEGB Rule

# x = 25
# def my_func():
#     x = 50
#     return x
# #
# # print x #25
# # print my_func() #50
#
# my_func()
# print x #25

# Enclosing Local Function
# name = "a global name"
#
# def greet():
#     name = "sammy"
#     def hel():
#         print name  #sammy
#     hel()
#
# greet()
# print name #a global name


# name = "a global name"
#
# def greet():
#     def hel():
#         print name  #a global name
#     hel()
#
# greet()

# Built-in
# x = 50
#
# def func():
#     global x   #redefined in global namespace
#     x = 100
#
# print x
# func()
# print x

# But we should avoid global variable, should use return instead
# x = 30
#
# def func():
#     x = 60
#     return x
#
# print x
# x = func()
# print x

# Oops
# In python everything is in form of object
# class Sample():
#     pass
#
# x = Sample()
#
# print x
# print type(x)

# class Dog:
#
#     # class object attribute
#     species = "mammal"
#
#     def __init__(self, breed):
#         self.breed = breed
#
# myDog = Dog(breed = "Lab")
# # or myDog = Dog("Lab")
# print myDog.breed
# print myDog.species

# Inheritance

# class Animal:
#
#     def __init__(self):
#         print "Animal"
#
#     def whoAmI(self):
#         print "Animal"
#
#     def eat(self):
#         print "eating"
#
# class Dog(Animal):
#      def __init__(self):
#         Animal.__init__(self)
#         print "Dog created"
#
#
# ma = Dog()
# ma.whoAmI()
# ma.eat()

# Special Methods

class Book:

    def __init__(self, title, author, page):
        self.title = title
        self.author = author
        self.page = page

    def __str__(self):
        return "Title: {}, Author: {}".format(self.title, self.author, self.page)

    def __len__(self):
        return self.page

    def __del__(self):
        print "b is destroyed"

b = Book("Python", "Harsh", 200)

print b

print len(b)

del b
