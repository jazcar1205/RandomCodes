blocks = int(input("Enter the number of blocks: "))
count = 1
height = 0 
    

while (blocks >= 0):
  blocks-=count
  if (blocks >= 0):
    count += 1
    height +=1
print("The height of the pyramid:", height)
