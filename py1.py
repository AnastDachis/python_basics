
#if u dont remember a specific function u can type 
#help()
help(abs)

#clear console python
import os
clear = lambda: os.system('cls')
clear()

a=2
b=5
print("b+a =",b+a)
print("b//a =",b//a)
print("b/a =",b/a)
print("b**a =",b**a)
print("absolute value =",abs(-(b/a)))

#defining a function
def return_j(a):
  j=abs(a)
return j

print(return_j(-88))

def mod_5(x):
  #"""Return the remainder of x after dividing by 5"""
return x % 5

print(
  'Which number is biggest?',
  max(100, 51, 14),
  'Which number is the biggest modulo 5?',
  max(100, 51, 14, key=mod_5),
  sep='\n',
)

#Using boolean
x = True
#Printing boolean values
print(x)
print(type(x))

#Boolean (TRUE or FALSE)
print(a==b)#FALSE
print(a!=b)#TRUE

#Function with boolean condition 
def is_odd(n):
  return (n % 2) == 1

print("Is 100 odd?", is_odd(10))#FALSE
print("Is -1 odd?", is_odd(-1))#TRUE

print(True or True and False)
#(True and False)=False
#True or False == True
print(True or False)#True

#lists
#string list
string_list = ['abs','deg','lal']
#sorted list
sorted(string_list)
#length of a list
len(string_list) 

#numeric list
num_list = [1,2,3,4,5]
#sum of a list(numeric)
sum(num_list)
#max
max(num_list)
#min
min(num_list)
#list append (adding) to the last position of the list
num_list.append(8)
#removing the last object of list
num_list.pop()
#finding a certain objects position
num_list.index(3)
# Is 3 a part of num_list?
'3' in num_list 
# False(why is it false?)

# Because '3' or "3" is a character and
# the 3 we are looking is a numeric value
# 3 is not the same as '3'

#How to find if 3 is a part of num_list ?
3 in num_list 
#True

#numeric complex(μιγαδικοι)
c=4+8j
#real part of c
print(c.real)
#imaginary part of c
print(c.imag)

#Loops(επαναληψεις)
# !!!Important when using a loop dont forget : , 
# !!!Σημαντικο οταν κανετε χρηση της επαναληψης μην ξεχνατε το :

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
  print(planet, end=' ') # print all on same line

#For - Loops using for numeric (Για range(n) κανε αυτο )
summ=0
i=0
n=len(num_list)
for i in range(n):
  summ=summ+num_list[i]
summ  

#while loop (Οσο γινεται κατι κανε αυτα)
i=0
while i<5:
  print(i," ")
  i+=1
