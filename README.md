# Git Intro Practice Repository Setup

## Repository 1: dyson-git-practice

### File Structure
```
dyson-git-practice/
├── README.md
├── .gitignore
├── requirements.txt
├── calculator.py
└── utils.py
```

---

## Setup Commands

```bash
# Create directory
mkdir dyson-git-practice
cd dyson-git-practice

# Initialize git
git init
git branch -M main
```

---

## File Contents

### README.md
```markdown
# Dyson Git Workshop - Practice Repository

Welcome to the Git practice repository!

## What's Included
- Simple calculator functions
- Utility functions for practice
- Requirements file for dependencies

## How to Use
1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate: `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run: `python calculator.py`

## Practice Tasks
During the workshop, you'll:
- Add new functions (multiply, divide)
- Commit your changes
- Push to GitHub
- Create branches
- Collaborate with teammates

Happy learning! 🚀
```

### .gitignore
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Project specific
*.log
temp/
```

### requirements.txt
```
# No external dependencies needed for basic workshop
# Participants can add dependencies if they extend the project
```

### calculator.py
```python
"""
Simple calculator for Git workshop practice
"""

def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract two numbers"""
    return a - b


# Participants will add multiply() and divide() functions during workshop


if __name__ == "__main__":
    print("Simple Calculator")
    print("=================")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print("\nAdd more functions during the workshop!")
```

### utils.py
```python
"""
Utility functions for the workshop
"""

def greet(name):
    """Greet a user"""
    return f"Hello, {name}!"


def calculate_average(numbers):
    """Calculate average of a list of numbers"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# Participants can add more utility functions here
```

---

## Git Commands to Create Repository

```bash
# Add all files
git add .

# Initial commit
git commit -m "Initial commit: Setup practice repository"

# Create on GitHub (do this manually on github.com)
# Then connect and push:
git remote add origin https://github.com/YOUR-USERNAME/dyson-git-practice.git
git push -u origin main
```

---

## For Participants During Training

```bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/dyson-git-practice.git
cd dyson-git-practice

# Check status
git status

# Make changes to files...

# Stage changes
git add calculator.py

# Commit
git commit -m "Add: Implemented multiply function"

# Push
git push
```

---

## Repository URL Format
`https://github.com/[YOUR-TRAINER-USERNAME]/dyson-git-practice`

Share this URL with participants!