
a = [2,4,'hello',9.0]

if 'hello' in a:
	print("Hey!")

num_list = [1,2,3,8.12,10,11,45,32,20,11,67,45,32,1,2,3,1,1]

print(sorted(num_list,reverse=True)) #Decending order

strings = ['a','bb','ccz','ques','hello','dahdms','dragon','Dandaelion','Geralt of Rivia']

# print(sorted(strings,key=len)) #sort based on length

def remove_duplication(data):
	list_sorted = sorted(data)

num_list.remove(1) # First occurrence of one will be removed

l = [[2,1],[8,6],[2,5],[3,3],[1,16]]

# print(sorted(l))

# list.insert(pos,value)

# print(num_list)

num_list.insert(0,12)

print(num_list)

print(num_list.pop()) # pop last element from the list

num_list.append(12) # append 12 to the last of the list

print(num_list) 