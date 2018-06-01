
a = [2,4,'hello',9.0]

if 'hello' in a:
	print("Hey!")

num_list = [1,2,3,8.12,10,11,45,32,20,11,67,45,32,1,2,3,1,1]

print(sorted(num_list,reverse=True)) #Decending order

strings = ['a','bb','ccz','ques','hello','dahdms','dragon','Dandaelion','Geralt of Rivia']

print(sorted(strings,key=len)) #sort based on length

def remove_duplication(list):
	list = sorted(num_list)

