
# List by Defintion #
my_list =[1,2,4,12,1,8]
print(my_list,"\n")

# List by Building #
print("List by Building")
my_list1= [ x for x in range (2,11,2)]
print(my_list1[0])
print(my_list1," \n")

# List by Slice #
print("List by Slice")
my_list2 =  my_list[:4]
print(my_list2)
my_list2 =  my_list[2:]
print(my_list2)
my_list2 =  my_list[:] #Copy Entire List
print(my_list2)
my_list2 =  my_list[3:5]
print(my_list2,"\n")


# List by Iteration through other List #
print("List by Iteration through other List")
my_list3 = []
for spot in my_list:
  my_list3.append(spot*2)
print(my_list3,"\n")


# 2D Lists #
print("2D Lists")
rows = [[" " for x in range(8)] for y in range(8)]
for rows in rows: print(rows)
print("\n")

# 3D Lists #
print("3D Lists")
boards = [[[" " for x in range(8)] for y in range(8)] for z in range(8)]
for board in boards: 
  for row in board:
    print(row)
  print("")
