#stride
print(myList{0:6:2}) #from index 0 to 6, skip by 2

#string are just lists

phrase = 'catch the dog'
phrase[2]
phrase[4]
phrase[-1:0:-3] #strides work backwards. -1 is right, 0 left, down 3
#accessing elements of a list
print(mylist[1])

#writing functions
def sumFunction(a,b):
return a+b
#calling functions
print(sumFunction(2,20))
 
#ifelse
if(x==10):
x=5
elif(y==-10);
y==5
else:
x=y-x

#loop
mylist=[1,3,8,412,43,2,20]

#length of list
len(mylist)

# for loop by index
for i in range(len(mylist)):
print my(mylist[i])

#for each loop
for val in mylist:
print(val)

#while
x=0
while(x<5):
    x+=1
    print(str(x))

#dictionaries
lookup={}
lookup['kc']='chiefs'
lookup['ne']='patriots'

#three data types at input

#string 
phrase = input("Enter string:")
print("Said" + phrase) #string concatenation
print(f"You said{phrase}") #formatted string literall

#float
someFloat = float(input("enter float"))
print("Entered float:" + str(someFloat))
print(f"Entered float:" {someFloat}")

#int
someInt = float(input("enter an int"))
print("ya entered " + str(someInt))
print(f"ya entered {someInt}")

#string interpolation is sweeeeet
print(f"Do python inline, like so: {someFloat}*{someInt}= {someFloat * someInt}")

