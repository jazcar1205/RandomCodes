global word 

secret_word = input("Give me a word: ")
word =[]
word_pic =[]

for i in secret_word:
  word.append(i)
  word_pic.append("*")
print(word_pic)


while(word != word_pic):
  word_guess= input("Give me a Letter! (only lower case \n")
  for i in secret_word:
    if ( word_guess == i):
      j = word.index(i)
      word_pic.pop(j)
      word_pic.insert(j,word_guess)
      print(word_pic)
    
  
    
print("\nSecert Word is: " + secret_word)
