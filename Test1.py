print("I count the length in word for a living, so go on type any word and i will count it for you")
word = input("Enter word to count: ")
print(word)


count = 0
length = len(word)
print("The length of the word is: ", length)

for _ in range(length):
  print(word[count])
  count = count + 1
  
import time
print("Closing in 10 seconds")
time.sleep(10)
print("End")