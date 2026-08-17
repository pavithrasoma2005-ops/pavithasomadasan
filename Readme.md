# Password Strength Checker

## What it does
This is a simple Python tool that checks how strong a password is and gives suggestions to improve it.

## How it works
The script checks a password against five criteria:
- Is it at least 8 characters long?
- Does it contain an uppercase letter?
- Does it contain a lowercase letter?
- Does it contain a number?
- Does it contain a special character (like !@#$%)?

Based on how many of these checks pass, the password is rated from "Very Weak" to "Very Strong," and the tool prints specific tips for anything that's missing.

## How to run it
1. Make sure Python is installed on your system
2. Download `password_checker.py`
3. Open a terminal and run:
4. Enter a password when prompted to see its strength rating

## What I learned
Working on this helped me understand how regular expressions (regex) can be used to search for patterns in text, like checking for specific character types in a string.
