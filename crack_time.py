def estimate_crack_time(password):
    length = len(password)

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    pool = 0

    if has_lower:
        pool += 26
    if has_upper:
        pool += 26
    if has_digit:
        pool += 10
    if has_symbol:
        pool += 32

    combinations = pool ** length

    guesses_per_second = 1000000000

    seconds = combinations / guesses_per_second

    if seconds < 1:
        return "Less than a second"
    if seconds < 60:
        return "A few seconds"
    if seconds < 3600:
        return "Minutes"
    if seconds < 86400:
        return "Hours"
    if seconds < 31536000:
        return "Months"
    if seconds < 31536000 * 100:
        return "Years"

    return "Centuries"