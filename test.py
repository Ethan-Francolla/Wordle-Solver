word_list = []
known_letters_list = ['l','e']
word1 = ['h','e','l','l','o']
word2 = ['a','d','i','e','u']
word3 = ['c','l','o','y','s']
word4 = ['w','r','u','n','g']
word_list.append(word1)
word_list.append(word2)
word_list.append(word3)
word_list.append(word4)

# Remove words from the word list that don't have all of the known letters
for letter in known_letters_list:
    for word in word_list:
        if letter not in word:
            print("removed",word)
            word_list.remove(word)
print(word_list)