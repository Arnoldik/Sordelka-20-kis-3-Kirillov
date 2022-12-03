s =input("Введите строку:")
count = 0
vowels = set("aeiou")
for letter in s:
    if letter in vowels:
        count += 1
print("Количество гласных равно:")
print(count)


