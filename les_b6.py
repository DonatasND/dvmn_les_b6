password = input("Введите пароль: ")

score = 0


def is_very_long(password):
    return 2 if len(password) > 12 else 0


def has_digit(password):
    return 2 if any(i.isdigit() for i in password) else 0


def has_upper_letters(password):
    return 2 if any(i.isupper() for i in password) else 0 


def has_lower_letters(password):
    return 2 if any(i.islower() for i in password) else 0 


def has_symbols(password):
    return 2 if any(i == "%" or i == "#"  for i in password) else 0 


funk = [
    is_very_long, 
    has_digit, 
    has_upper_letters, 
    has_lower_letters,
    has_symbols,
]

for i in funk:
    score += i(password)


print('Рейтинг пароля:', score)
