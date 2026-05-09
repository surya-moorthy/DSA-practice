sentence = input("Enter the sentence : ")

idx = 0

words = sentence.split()

for i in range(len(words)):
    if(len(words[idx]) < len(words[i])):
        idx = i

print("longest word in the given sentence :", words[idx])