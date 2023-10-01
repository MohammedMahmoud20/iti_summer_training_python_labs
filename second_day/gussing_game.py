import random

random_words = ["apple", "banana", "cherry", "orange", "grape", "kiwi"]
counter = 0

name = input("Enter your name: ")
random_w = random.choice(random_words)
word = "X" * len(random_w)

while counter < 7:
    print(word)

    alpha = input("Guess an alphabet: ")

    if alpha in random_w:
        for i in range(len(random_w)):
            if random_w[i] == alpha:
                word = word[:i] + alpha + word[i+1:]

        if "X" not in word:
            print(f" the word was {random_w}\n you won ")
            break
    else:
        print(" guess another alphabet ")
        counter += 1

if counter == 7:
    print(f"You lost, The word was {random_w}")
