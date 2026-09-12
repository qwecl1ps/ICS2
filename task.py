a = int(input("Введіть перше двоцифрове" ))
b = int(input("Введіть друге двоцифрове" ))

first_digit1 = a // 10
first_digit2 = b // 10

product = first_digit1 * first_digit2

print(f"Перша цифра першого числа: {first_digit1}")
print(f"Перша цифра другого числа: {first_digit2}")
print(f"Добуток перших цифр: {product}")

