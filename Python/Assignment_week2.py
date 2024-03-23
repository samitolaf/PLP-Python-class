#creating an empty list
my_list = []
#append elemnents to list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list = ['10', '20', '30', '40']
my_list.insert(2, 15)
print(my_list)

#Extend my list 
my_list = ['10', '20', '30', '40']

List_B = ['50', '60', '70']
my_list.extend(List_B)
print(my_list)
#removing the lasst element from My_list
my_list = ['10', '20', '30', '40']
my_list.pop()
print(my_list)
#.remove method is used by calling the object while .pop is used to remove solely the last element on the list
# my_list.remove('40')
my_list = ['10', '20', '30', '40']
my_list.sort()
print(my_list)

#index 
my_list = ['10', '20', '30', '40']

# Find and print the index of '30'
index_of_30 = my_list.index('30')
print("Index of '30':", index_of_30)

#check for index of 30
print(f"Final List:", my_list)
#print(f"Index of 30:", index_of_30)