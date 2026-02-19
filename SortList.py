my_list = [1,2,4,4,1,4,2,6,2,9]

print("Max:", max(my_list))
print("Max:", min(my_list))

#Ascending
my_list.sort()
print(my_list)
print("Max: ", my_list[-1])
#Desending
my_list.sort(reverse = True)
print(my_list)
print("Max: ", my_list[0])