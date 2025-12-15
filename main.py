
import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''
print("Добро пожаловать в генератор паролей!")
count = int(input("Введите количество паролей для генерации: "))
length = int(input("Введите длину одного пароля: "))
include_digits = input("Включать цифры 0123456789? (да/нет): ").lower().strip() == 'да'
include_uppercase = input("Включать прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да/нет): ").lower().strip() == 'да'
include_lowercase = input("Включать строчные буквы abcdefghijklmnopqrstuvwxyz? (да/нет): ").lower().strip() == 'да'
include_punctuation = input("Включать символы !#$%&*+-=?@^_? (да/нет): ").lower().strip() == 'да'
exclude_ambiguous = input("Исключать неоднозначные символы il1Lo0O? (да/нет): ").lower().strip() == 'да'
if not (include_digits or include_uppercase or include_lowercase or include_punctuation):
    print("\nОшибка: Не выбран ни один тип символов для пароля!")
    print("Пожалуйста, включите хотя бы один набор символов.")
    exit()
chars = ''
if include_digits:
    if exclude_ambiguous:
        digits_filtered = digits.replace('0', '').replace('1', '')
        chars += digits_filtered
    else:
        chars += digits
if include_uppercase:
    if exclude_ambiguous:
        uppercase_filtered = uppercase_letters.replace('I', '').replace('O', '')
        chars += uppercase_filtered
    else:
        chars += uppercase_letters
if include_lowercase:
    if exclude_ambiguous:
        lowercase_filtered = lowercase_letters.replace('i', '').replace('l', '').replace('o', '')
        chars += lowercase_filtered
    else:
        chars += lowercase_letters
if include_punctuation:
    chars += punctuation
if not chars:
    print("\nОшибка: После исключения неоднозначных символов не осталось доступных символов для генерации пароля!")
    print("Пожалуйста, измените настройки или отключите исключение неоднозначных символов.")
    exit()
def generate_password(length, chars):
    """Генерирует пароль заданной длины из указанных символов"""
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password
print("Сгенерированные пароли:")
for i in range(count):
    password = generate_password(length, chars)
    print(f"{i + 1}. {password}")