# Lists:
# Given a list of integers, return the sum of all elements.
nums= [1,2,3,4]
print(len(nums)) # length of list
print(nums[0]) # accessing the list items.
nums[0:1]=[5,6] # updating list items
print(nums) # result-[5,6,3,4]
nums.append(9) # add list item at the end.
print(nums)
nums.insert(0,20) # to insert item in specific index.
print(nums)
nums.reverse() # reverse regardless of alphabets.
print(nums)
nums.sort(reverse=True)
print(nums)



# Merging two lists:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple) # extending the list
print(thislist) 

# Remove Specified Item:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#If you do not specify the index, the pop() method removes the last item.
# The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


# Clear the List:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Sort List Alphanumerically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort Descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True) # reverse=true
print(thislist)

# What if you want to reverse the order of a list, regardless of the alphabet?:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse() # reverse regardless of the alphabets.
print(thislist)

# Copy a List:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# another way use list():
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#=====================================================Questions===================================

#

