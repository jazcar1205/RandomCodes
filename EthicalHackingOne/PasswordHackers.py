import string

secret_password = "$p3"
guess = ""
guess_list = []
myList = []

for num in range (10):
  myList.append(str(num))

for ltr in list(string.ascii_uppercase):
  myList.append(ltr)

for ltr in list(string.ascii_lowercase):
  myList.append(ltr)

for ltr in list(string.punctuation):
  myList.append(ltr)

for a in myList:
  for b in myList:
    for c in myList:
      for d in myList:
      myList.append(a+b+c)


for guess in guess_list:
  if (guess == secret_password):
    break
  
print("PASSWORD IS", guess)