def find_longest_words(string):
    longest_words = []
    max_length = 0
    string_list = string.split()
    
    for word in string_list:
        if len(word) > max_length:
            longest_words = [word]
            max_length = len(word)
        elif len(word) == max_length:
            longest_words.append(word)

    return longest_words

# Collect words from user input
words = ""
for _ in range(6):
    word = input("What words do you want to compare? Enter separately: ")
    words += f" {word}"

# Print the longest word or words
longest_words = find_longest_words(words)
print("Longest word(s):", ", ".join(longest_words))
