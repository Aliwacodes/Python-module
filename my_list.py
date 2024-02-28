#empty list
my_list=[]
print ("Before append",my_list)
#append the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After append", my_list)
#insert the value 15 in the second position
my_list.insert(1,15)
print("after insert", my_list)
#extend the list
my_list.extend([50,60,70])
print("after extend",my_list)
#remove last element
my_list.pop()
print("after deletion",my_list)
#sort in ascending order
my_list.sort()
print("after sorting",my_list)
#find the index of value 30
index=my_list.index(30)
print("index of 30", index)