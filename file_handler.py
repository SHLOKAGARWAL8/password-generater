from datetime import datetime


def save_password(password, strength):
    with open("password_history.txt", "a") as file:
        file.write("=" * 40 + "\n")
        file.write(f"Date & Time : {datetime.now()}\n")
        file.write(f"Password    : {password}\n")
        file.write(f"Strength    : {strength}\n\n")