def print_in_frame(sentence):
    length = len(sentence)
    frame_line = '#' * (length + 4)
    
    print(frame_line)
    print(f"# {sentence} #")
    print(frame_line)

# Example usage
sentence = input("Enter a sentence: ")
print_in_frame(sentence)