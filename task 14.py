word = input("Enter a word: ")

# casefold() ignores uppercase/lowercase differences.
normalized_word = word.casefold()

if normalized_word == normalized_word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")