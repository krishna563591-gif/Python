#List-we can store any type of data & access them.
friends= ["Apple","Orange",5,345.06,"False","Akash","Rohan"]
print(friends[0]) # Apple
print(friends[6]) # Rohan

# Difference Between List & String-in list we can change any string in list but not in string.


# List Methods:
# Append Methods-add at the end of list
friends= ["Apple","Orange",5,345.06,"False","Akash","Rohan"]
print(friends) 
friends.append("Harry")
print(friends) # Apple Orange 5 345.06 False Akas Rohan Harry


#Sort Methods
l1=[24,54,767,2,8,9]
l1.sort()
print(l1) #2 8 9 24 54 767

#reverse Method: l1.reverse()
#insert Method: 
l1.insert(3,3333) #iNSERT 3333 at the place of index 3.
print(l1)


# pop method: it pop out the selected index.
l1.pop(3)
print(l1)


# remove method: it remove particular value.
#clear method
#index method
#count method
#copy method
# extend method
