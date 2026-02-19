user_word= input("Give me a word: " )
user_word = user_word.upper()


for ltr in user_word:
  if (ltr not in ("A","E","I","O","U")):
      print(ltr)