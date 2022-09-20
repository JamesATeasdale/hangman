word = [i for i in input("Enter your word here: ")]
guessed = [int(i) for i in range(len(word))]
count = 5
print(guessed)

while count > 0:
    guess = input("Guess a letter: ")
    
    while guess in word:
        guessed[word.index(guess)] = guess
        word[word.index(guess)] = "null"
    print("Correct!")
    print(guessed)
    if all([isinstance(item, str)for item in guessed]):
        print("You Win!")
        break

    else:
        count -= 1
        print("Letter not in word! guesses left: " + str(count))
        print(guessed)
        
print("Goodbye!")
