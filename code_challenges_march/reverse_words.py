def reverse_words(sentence):
    words = sentence.split()  # Split the sentence into words
    reversed_words = words[::-1]  # Reverse the list of words
    reversed_sentence = ' '.join(reversed_words)  # Join the reversed list back into a string
    return reversed_sentence

sentance = input("give me a sentance:>")
print(reverse_words(sentance))