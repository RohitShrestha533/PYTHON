# 🐍 Python Learning Repository

A personal collection of Python scripts, exercises, and mini-projects built while learning Python from the ground up — covering core language fundamentals, data structures, OOP, functional programming patterns, file I/O, and a Django web application.

---

## 📁 Repository Structure

```
PYTHON/
├── 📄 Core Python Scripts
│   ├── Basic.py            # Variables, lists, sets, loops, dicts, functions
│   ├── basics.py           # Foundational syntax experiments
│   ├── Practice.py         # Scratch practice
│   ├── classes.py          # OOP — Flight class with seat management
│   ├── datastructure.py    # Lists, tuples, dicts, sets in action
│   ├── decorator.py        # Python decorator pattern
│   ├── distionary.py       # Dictionary operations
│   ├── exception.py        # Exception handling with try/except/sys.exit
│   ├── lambda.py           # Lambda expressions, map(), filter()
│   ├── list.py             # List operations and methods
│
├── 🎯 Mini Projects
│   ├── Calculator.py       # CLI calculator (add, subtract, multiply, divide)
│   ├── Game.py             # Rock-Paper-Scissors game with score tracking
│   ├── Diamond.py          # Diamond star pattern generator
│
├── 📈 Levelled Practice
│   ├── level1.py           # Loops & Conditions (primes, factorials, palindromes)
│   ├── level2.py           # Intermediate exercises
│   ├── level3.py           # Advanced challenges
│
├── 📂 assignments/         # 100 structured Python practice problems
│   ├── question.py         # Full question bank (variables → functions)
│   ├── ass1.py – ass10.py  # Individual assignment solutions
│   └── recursive.py        # Recursion exercises
│
├── 📂 opp/                 # Object-Oriented Programming examples
│   └── acc.py              # Bank Account class (debit, credit, balance)
│
├── 📂 file/                # File I/O exercises
│   ├── file.py             # Reading and writing files
│   ├── practice1.py / practice2.py   # File handling practice
│   └── *.txt               # Sample text files
│
└── 🌐 Django Web App — Student Management System
    ├── manage.py           # Django entry point
    ├── cms/                # Project settings, URLs, WSGI/ASGI
    └── student/            # Django app — full CRUD for students
        ├── models.py       # Student model (name, email, phone, address, course)
        ├── views.py        # Add, display, edit, update, delete views
        ├── urls.py         # URL routing
        ├── admin.py        # Django admin registration
        └── templates/      # HTML templates for the student app
```

---

## 🧠 Topics Covered

| Category | What's Inside |
|---|---|
| **Variables & Types** | Integers, strings, booleans, type conversion |
| **Control Flow** | `if/elif/else`, ternary, nested conditions |
| **Loops** | `for`, `while`, `range()`, `break`, `continue` |
| **Functions** | Defining functions, return values, default args |
| **Data Structures** | Lists, tuples, sets, dictionaries |
| **OOP** | Classes, `__init__`, methods, objects, encapsulation |
| **Functional Python** | `lambda`, `map()`, `filter()`, decorators |
| **Exception Handling** | `try/except`, `ZeroDivisionError`, `ValueError`, `sys.exit()` |
| **File I/O** | Reading and writing `.txt` files |
| **Django (Web)** | Models, Views, Templates, URLs, MySQL database, CRUD |

---

## 🚀 Mini Projects

### 🧮 Calculator (`Calculator.py`)
A command-line calculator supporting the four basic operations.

```
1. Addition
2. Subtract
3. Multiply
4. Divide
Choose calculation number: 1
First number: 10
Second number: 5
The resultant Addition of 10 and 5 is: 15
```

---

### ✊ Rock-Paper-Scissors (`Game.py`)
An interactive CLI game against the computer with live score tracking.

```
Enter rock, scissors, paper or 'exit' to stop the game: rock
You win this round
Your choice: rock
Computer choice: scissors
Score: You 1 - Computer 0
```

---

### 💎 Diamond Pattern (`Diamond.py`)
Prints a diamond shape of `*` characters of any size.

```
Enter number of rows you want in diamond: 4
   *
  ***
 *****
*******
 *****
  ***
   *
```

---

### 🏦 Bank Account (`opp/acc.py`)
An OOP-based account simulation with debit, credit, and balance checking.

```python
c1 = Account(balance=10000, account_no=123)
c1.debit(5000)   # Balance: $5000
c1.credit(2000)  # Balance: $7000
```

---

### 🎓 Student Management System (Django)
A full-stack web CRUD app for managing student records backed by a MySQL database.

**Features:**
- ➕ Add a new student (name, email, phone, address, course)
- 📋 List / display all students
- ✏️ Edit and update student records
- 🗑️ Delete a student

**Stack:** Django 5 · Python · MySQL (`studentdb`) · HTML templates

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.8+
- pip

### Running Standalone Scripts

```bash
# Clone the repository
git clone https://github.com/RohitShrestha533/PYTHON.git
cd PYTHON

# Run any script directly
python Calculator.py
python Game.py
python Diamond.py
```

### Running the Django Student Management System

1. **Install dependencies**

   ```bash
   pip install django pymysql
   ```

2. **Set up the MySQL database**

   Create a database named `studentdb` in your local MySQL instance:

   ```sql
   CREATE DATABASE studentdb;
   ```

3. **Apply migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Start the development server**

   ```bash
   python manage.py runserver
   ```

5. **Open in browser**

   Navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📚 Assignments

The `assignments/` folder contains solutions to **100 structured Python problems** organised by topic:

| Range | Topic |
|---|---|
| 1–10 | Basic Python & Variables |
| 11–20 | Input & Output |
| 21–35 | Conditional Statements |
| 36–55 | Loops |
| 56–70 | Lists |
| 71–80 | Tuples & Sets |
| 81–90 | Dictionaries |
| 91–100 | Functions |

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0-092E20?style=flat&logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=flat&logo=mysql&logoColor=white)

---

## 👤 Author

**Rohit Shrestha**

> 💡 This repository documents a personal Python learning journey — from "Hello, World!" to building a full Django web application.
