"""
Write a function to determine the number of vowels in a string
def count_vowels(s):
 
This function should return an integer and doesn't count "y" as a vowel.
"""


def count_vowels(text):
    count = 0
    for char in text:
        if char.lower() in "aeiou":
            count += 1
    return count

print(count_vowels("adsfjaIsda")) 
print(count_vowels("!@#Oa||"))
print(count_vowels("ab32cdaio&"))