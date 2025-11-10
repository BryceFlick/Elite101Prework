def sum_of_digits(text):
    count = 0
    for char in text:
        if char.isdigit():
            count += int(char)
    return count

print(sum_of_digits("adsfjagsda")) 
print(sum_of_digits("1234134123412"))