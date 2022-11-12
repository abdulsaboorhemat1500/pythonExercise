from collections import namedtuple ,deque , ChainMap ,Counter , OrderedDict ,defaultdict

# Namedtuple example
a = namedtuple('courses' , 'id,name , tech ')  # the first index is for tuple name 
s = a._make([22,'data science' , 'python'])

print(s)

creating a deque
 
a = ['d' , 'u' , 'r' , 'e' , 'k']  # first we create list to assign that to deque 
a1 = deque(a) # creating deque
print(a1)
	
a1.append('a') #adding in the right side
print(a1)
a1.appendleft('e') # adding in the left side
print(a1)

a1.pop()  # delelting from the right side 
print(a1)
a1.popleft()   # deleleting from the left side 
a1.extend('1')  # same as append 
a1.extend('9')
print(a1)


example of chainmap 
a = { "id" : 1 , "name": "saboor"} # first dictionary
b = { "homenumber" : 33 , "lastname": "hemat"}  #second dictionary

list_dic=ChainMap(a,b)  #create chain map for two dictionary
print(list_dic)

list_dic=list_dic.new_child({"number" : "098890" , "course" : "advance programming"})
# added new child to chain map coll
print(list_dic)


# example fo counter  
a = [1,1,1,1,2,3,3,4,3,3,4] # creating list for counting hashable objects

print(Counter(a))  # printing hashable objects via  Counter)()


 ordered dictionary 

od = OrderedDict()  # creating od as  Ordered Dictionary 
od[1] = 'e'
od[2] = 'd'
od[3] = 'u' # inserting values 
od[4] = 'r'
od[5] = 'e'
od[6] = 'k'
od[7] = 'a'
od[1] = 'z'
print(od)

creating built in dictionary
my_dictionary = {
   '1' : 'e' ,
   '2' : 'd',
}

my_dictionary[3] = 'j'
my_dictionary[4] = 'w'
my_dictionary[5] = 'q'
my_dictionary[3] = 'p'
print(my_dictionary)

# creating default dictionary 

d = defaultdict(int)  # creating default dict and also define its type 

d[1] = 'edureka'
d[2] = 'python'
print(d[6])

# bellow are some examples of built in collection like list, tuples , set and dictionary 
# the first one is list 

myList = [1,2,3,"saboor hemat " , True , 1.4 , 'e']
# we can add any types of data in the list list is mutable and it is unorder 
myList.append("afghanistan") # add new value in the end of the list 
# myList.clear() # clear the whole list 
newlist = myList.copy() # it get a copy of list and store it in another variable 
print(myList.count(3)) # take one arguement and find how many time it repeated
myList.extend("hello") #''' it take iterable object and iterate on that object and create 
# new index in list for each Iteration '''
print(myList.index('h')) # find the index of value 
myList.insert(4,"new added value") # adding value in particular index 
myList.pop(4) # it remove particular index from the list  via index 
myList.remove("saboor hemat ") # it remove particular value via inserting value name 
print(myList.reverse()) # it reverse the list 
myList.sort()  # if the list is from one type this function return the sorted list 
print(newlist)
print(myList)

# now the second built in collection is tuple  
# tuple is immutable and it does not have many function coz of immutable

mytuple = (2 ,2,4,5,6,7,8,3,("saboor" ,  "hemat"),3,3,3) # tuple inside tuple 
print(mytuple.count(("saboor" , "hemat"))) # it return how many time is repeated
print(mytuple.index(2)) # it return the first index when it accured 
print(mytuple)

accessing tuple via index 
print(mytuple[-1]) # it well print the last index of the tuple 
print(mytuple)

'''tuple is unchangeable in python  but we can change its value in the way 
first we change tuple to list then we change the value and again change the list to 
tuple'''
# we can also unpake the whole tuple  

tup = ("laptop" , "saboor" , "hemat") # creating tuple 

(computer,name,lastname) = tup  # unpakking tuple into variables 
print(computer)
print(name)
print(lastname)

# we had only two methods using with tuples
# set examples  A set is a collection which is unordered, unchangeable*, and unindexed.
# unordered and does not have doplicate values 
myset = {"home", "saboor" , "hemat" , 1234}
print(myset)
print("home" in myset) # it print only boolen value
# we can't access the value via index we have to iterate with loop
# but we can add item  via add() function
sec_set = {"about" , "cs"} # creating new set for inserting in the the first one
myset.add("this is new value")
myset.update(sec_set) # we use update() function for updating the first one 
# # and we can add any type of iterable into set collection

myset.remove("about") # it remove the about index but if there is no such value 
# it well raise error
myset.discard("cs") # it also remove the cs value but with no error
''' we can also use pop() function but as we know set is unordered so we don't 
know which value well be deleted in pop calling
del function delete the whole set 
and clear function clear the whole set 
'''
for i in myset:
   print(i)    # loop for accessing each el
print(myset)

union_set = myset.union(sec_set)
print(union_set)

'''               dictionary           '''

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print("before updating the dict : ",x) #before the change
car["color"] = "white"
print("After updating the dict : " , x) #after the change 

''' accessing dictionary elements '''

print(car["color"])  # print the value of color key 
print(car.get("color")) # also print the value of the color key 

x = car.keys() # can access to all key via key() function
print(x)
''' changing value '''
car.update({"color" : "red"}) # change the value 
car.update({"name" : "saboor"}) # and also we can add new item
print(car)

'''  we can remove item via  pop() function which take an arguement  and via popitem() funcion which remove item from the right side of the dict and  del() function delete the 
dect  and we have clear function which clear the dict '''

''' looping on dictionary '''

for x in car:
   print(x) # print only keys 
   print([x]) # print the values

for x in car.keys():
   print(x)

for x in car.values()
   print(x)

for x,y in car.items():
   print(x , y )  # x is key and y is value 

''' nested dict '''

di1 = {
   "name" : "saboor",
   "email" : "sabor@gmail.com"
}
di2 = {
   "id" : 234,
   "address" : "somewhere"
}

di3 = {
   "item1" : di1,
   "item2" : di2
}
print(di3)







