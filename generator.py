import string
import secrets


def generate_password(
    length,
    use_upper,
    use_lower,
    use_digits,
    use_symbols,
    keyword=""
):
    if length < 4:
        return "Password length must be at least 4."

    characters = ""

    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "You must select at least one character type."

    password = []

    if keyword:
        password.extend(list(keyword))

    if use_lower:
        password.append(secrets.choice(string.ascii_lowercase))

    if use_upper:
        password.append(secrets.choice(string.ascii_uppercase))

    if use_digits:
        password.append(secrets.choice(string.digits))

    if use_symbols:
        password.append(secrets.choice(string.punctuation))

    while len(password) < length:
        password.append(secrets.choice(characters))

    password = password[:length]

    secrets.SystemRandom().shuffle(password)

    return "".join(password)