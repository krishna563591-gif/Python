# Create a list by taking input from users 10-12 items and take target input from user and serch 1 by 1 in the list and show the respective indexing number of that target number.
my_list=[]
n=int(input("Enter the number of items you want to add in the list: "))
for i in range(n):
    item1=input("Enter the item: ")
    my_list.append(item1)
target=input("Enter the target item: ")
if target in my_list:
    index=my_list.index(target)
    print(f"The target item is found at index: {index}")
else:
    print("The target item is not found in the list.")

