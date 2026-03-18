#List-we can store any type of data & access them.
# related datas are stored in list.we call array in js.
# we can store any type of data in list such as string,number,boolean,list etc.


#example:
friends= ["Apple","Orange",5,345.06,"False","Akash","Rohan"]
print(friends[0]) # Apple
print(friends[6]) # Rohan

# Difference Between List & String-in list we can change any string in the list but not in the string.


# List Methods: 
# Append Methods-add at the end of list
friends= ["Apple","Orange",5,345.06,"False","Akash","Rohan"]
print(friends) 
friends.append("Harry")
print(friends) # Apple Orange 5 345.06 False Akas Rohan Harry

#=======================================================
# Sort Methods:sort the list in ascending order.
l1=[24,54,767,2,8,9]
l1.sort()
print(l1) #2 8 9 24 54 767
#=======================================================
#reverse Method: l1.reverse(): it reverse the list.
l1.reverse()
print(l1) #767 54 24 9 8 2 

#========================================================
#insert Method: l1.insert(index, value): it insert the value at the given index.
l1.insert(3,3333) #iNSERT 3333 at the place of index 3.
print(l1)

#========================================================

# pop method: l1.pop(index): it remove the item at the given index. if we don't give any index it remove the last item from the list. EXAMPLE:  

l1.pop(3)
print(l1) #767 54 24 9 8 2 ---> 3333 is removed from the list.
l1.pop() #it remove the last item from the list.
print(l1) #767 54 24 9 8 2 ---> 2 is removed from the list.


#==================================================
# remove & clear method: it clear the whole list.EXAMPLE:
l1=[1,2,3,4,5]
l1.remove(3) #it remove 3 from the list.
print(l1) #1 2 4 5  
l1.clear() #it clear the whole list.
print(l1) #[]   

#==================================================
#index method: it return the index of the first occurrence of the value. EXAMPLE:
l1=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5]
print(l1.index(1)) #0   

#==================================================
#count method: it return the count of the value in the list. EXAMPLE:
l1=[1,2,3,4,5,6,7,8,9,10,1,1,3,4,5]
print(l1.count(1)) #3  because 1 is present 3 times in the list.   

#================================================

#copy method: it return the copy of the list. EXAMPLE:
l4=[1,2,3,4,5]
l5=l4.copy()
print(l5) #1 2 3 4 5    

#=================================================

#extend method: it extend the list by adding all the items of another list. EXAMPLE:
l2=[1,2,3]
l3=[4,5,6]
l2.extend(l3)       
print(l2) #1 2 3 4 5 6


#=====================================Shallow Copy & Deep Copy========================================
#Shallow Copy: it creates a new list but the items in the new list are references to the items in the original list. EXAMPLE:
l6=[1,2,3,4,5]
l7=l6.copy() #shallow copy
print(l7) #1 2 3 4 5
l7[0]=100 # when we change the value of l7 it does not affect l6 because l7 is a shallow copy of l6 so when we change the value of l7 it does not affect l6.
print(l7) #100 2 3 4 5
print(l6) #1 2 3 4 5  because l7 is a shallow copy of l6 so when we change the value of l7 it does not affect l6.

#Deep Copy: it creates a new list and the items in the new list are not references to the items in the original list. EXAMPLE:
import copy
l8=[1,2,3,4,5]
l9=copy.deepcopy(l8) #deep copy
print(l9) #1 2 3 4 5
l9[0]=100 # when we change the value of l9 it does not affect l8 because l9 is a deep copy of l8 so when we change the value of l9 it does not affect l8.
print(l9) #100 2 3 4 5
print(l8) #1 2 3 4 5 because l9 is a deep copy of l8 so when we change the value of l9 it does not affect l8.

#Difference Between Shallow Copy & Deep Copy: in shallow copy the items in the new list are references to the items in the original list but in deep copy the items in the new list are not references to the items in the original list.   
    
#=========================================================