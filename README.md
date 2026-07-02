# 🔐 Password Generator

A secure and customizable password generator built with Python. This application allows users to generate strong passwords based on their preferences, evaluate password strength, estimate crack time, and save generated passwords for future reference.

---

## 📸 Demo

![Password Generator Demo](images/demo.png)

---

## ✨ Features

- Generate secure random passwords
- Generate multiple passwords at once
- Keyword-based password generation
- Choose character types:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Symbols
- Password strength analysis
- Password crack time estimation
- Automatically saves password history
- Modular and organized Python project

---

## 🛠 Technologies Used

- Python 3
- Python Standard Library
  - `secrets`
  - `string`
  - `datetime`

---

##  Project Structure

```
password-generator/
│
├── images/
│   └── demo.png
├── main.py
├── generator.py
├── strength.py
├── crack_time.py
├── file_handler.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

##  Getting Started

### Clone the repository

```bash
git clone https://github.com/SHLOKAGARWAL8/password-generator.git
```

### Navigate to the project

```bash
cd password-generator
```

### Run the application

```bash
python main.py
```

---

##  Example Output

```
=============================================
      PYTHON PASSWORD GENERATOR
=============================================

Enter password length: 16
How many passwords do you want? 3

Password Generation Mode
1. Random Password
2. Keyword Based Password

Choose option (1/2): 2
Enter your keyword: shlok

Generated Passwords
---------------------------------------------

1. sHl0k@92Q!Lm
   Strength : Strong 
   Crack Time : Centuries
```

---

##  Future Improvements

- Desktop GUI using Tkinter
- Copy password to clipboard
- Export password history to CSV
- Dark mode interface
- Password analytics dashboard
- Exclude confusing characters
- Custom symbol selection

---

##  Author

**Shlok Agarwal**

GitHub: https://github.com/SHLOKAGARWAL8

---


If you found this project useful, consider giving it a ⭐ on GitHub.