def anagram (str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    str1 = sorted(str1)
    str2 = sorted(str2)

    return str1 == str2

print("welcome to the animgram cheacker")
str1 = input("what is the first word:>")
str2 = input("what is the second word:>")

print(anagram(str1, str2))