# #create a function
# #pass in int as# parameter
# #loop through the range of 100 and 200
# #create a conditionof div by seven
# #create an 
def divisible_by_seven():
    

    seven=[n for n in range(100,200) if n%7==0] #only prints out the condition and not the value

    print(seven)
divisible_by_seven()
#  #programme for finding symmetrical numbers,
#  #create a string and find the mid point
#  #with the midpoint divide the string into two halves
#  #compare the two halves using slicing 
#  #if equal word is symmetrical 
def symm(dobi):
    # dobi="originals"
    p=len(dobi)//2
    if dobi[0:p]==dobi[p+1:]:
        print(f"{dobi} is a symmetrical word")
    else:
        print("This is not a symmetrical")
symm("mum") 
#     #print half of string to upper
# #   create a string
# #using len function try to find midpoint
# #using while loop,with condition less midpoint ,try for loopit
#create empty string
#Assign it each variable and upper.


#condition it to less<the misdpoint .toUpper
#create increased the variable




# 
# #print i with join and upper
# height="short"
#     x=0
#     while x<middle:
#        print(height(x))
#     # str(x)for x in height 
# capital()  
   #using for loop with range up to mid point
   #print each character to upper.

# def words(a):
#       mid=len(a)//2
#     #   x=range(a[0],mid)
#     i=0
#       pot=""
#       for x in a:
#         # print(x)
#         pot+=a(x).upper()
#         print(pot)
#     #   for y in range(mid):
#             # pri/nt("Hello")
#             # print(f"{y}")
        


#     #   print(f"{b} is the one in upper,whole string is {a}")
# # words("originals")
# #     #print half of string to upper
# #   create a string
# #using len function try to find midpoint
# #using while loop,with condition less midpoint ,try for loopit
#create empty string
#Assign it each variable and upper.

def wordsing(a):

    mid=len(a)//2     #find a midpoint that divides the string into two halves
    strinngz=""      #empty string '
    i=0               #default starting variablee 0
    for x in a:      #loop through the characters of each string
        if i<mid:  #i is in index      #condition for the index of the values up to mid
            strinngz+=a[i].upper()   #assign each value ega[i],you get the characters .upper
            i+=1                   #Assign it to the new string
        else:
            strinngz+=a[i]      #increament the value of i to cover the next
            i+=1                #else to print the rest values.


    print(strinngz)             #print string  
                                 #end function
wordsing("originals")   
def slice(b):
    middl=len(b)//2
    p=b[0:middl].upper()
    c=b[middl:]
    print(p+c)
slice("originals")
  #create midpoint to divide string into two halves
#using list comprehension
#create empty list
# inside the list 
#print each character to upper and create if condition,
#and else condition as well
#then for n in string
z="People"
lis=[print(z[i]).upper() if i>len(z)//2 else (z[i]) for x in z]
  
  






