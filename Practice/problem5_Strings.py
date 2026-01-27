name="krishna"
#print("firstcharacter:",name[0]) #k
#print("lastcharacter:",name[-1]) #a
#print("slice string:",name[0:3]) #kri

print("name:",name[-4:-1]) # shn -excludeing index -1
print("name:",name[1:4]) # ris -excluding index 4


#print("sliced string(0-4):",name[0:4]) #kri 
#print("sliced string(2-6):",name[2:6]) #ishn
#print("sliced string(:5):",name[:5])   #krishna
#print("sliced string(3:):",name[3:])   #shna
#print("sliced string(-4:-1):",name[-4:-1])  #sha
#print("sliced string(-6:):",name[-6:])  #r
#print("sliced string(:-3):",name[:-3])  #krishna
#print("sliced string(:):",name[:])  #krishna
#print("sliced string(-):",name[-])  #krishna
print(name[1:]) #rishna- excludeing index 0,but not excludeing last index
print(name[:4]) #kris -excludeing index 4,but not excludeing first index

print(name[-5:]) #ishna -excludeing index -6,but not excludeing last index
print(name[:-2]) #krish -excludeing index -2,but not excludeing first index
print(name[-6:-2]) #rish -excludeing index -2,but not excludeing index -6

#----------------------------------------QNA---------------------------------------------------
# Write a python program to display a user entered name followed by Good Afternoon input() function.
name=input("enter your name:,")
print(f"Good Afternoon:,{name}")

# Write a python program in a letter  template given below with name & date.
#letter='''
#Dear=<|Name|>,
#You are selected!
#<|Date|>
#'''
#print(letter.replace("<|Name|>","Krishna")).replace("<|Date|>","24 september 2050")
#
## Write a programm to dtect double space in a string.
name= "Harry is a good boy and"
print(name.find("  ")) # if result came -1 then there is no double space. if its any number than -1 then there is space.

# Replace the double space by with single space.
name= "Harry is a good boy and"
print(name.replace("  "," ")) 

#strings are emmutable -which means you can not change then by running functions on them.

# Write a program to format following sentence using escape sequencing.
#letter="Dear Krishna,this python course is nice. Thanks!"
letter="Dear Krishna,\n\t This python course is nice.\n Thanks!"
print(letter)



      