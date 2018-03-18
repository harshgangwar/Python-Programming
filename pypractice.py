

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


# Functions
# def

# 'filter' Functions
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# can be replaced by lamda function
def even_bool(num):
    return num%2 == 0

# lamba expression
evens = filter(lambda num: num%2 == 0, ls)

# filter
#evens = filter(even_bool, ls) #takes 2 args first is functios and sec list/tuple/string

print evens
