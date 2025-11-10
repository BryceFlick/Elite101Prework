user_input = input("Enter a word or list of words: ")

remove_spaces = ''.join(user_input.split())

remove_punctiation = remove_spaces.replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace("'", "").replace(":", "").replace(";", "")

test_string = remove_punctiation.lower()

reversed = test_string[::-1]

if test_string == reversed:
    print("The string is a palindrome.")

if test_string != reversed:
    print("The string is not a palindrome.")