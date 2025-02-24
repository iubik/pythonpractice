word = input("Enter a word: ")
new_word = ''

for letter in word:
	if letter == 'a':
		new_word += ('0')
		continue
	
	else:
		new_word += letter

print(new_word)