# STAT 386 Python Fluency Check

This assessment checks whether you are comfortable enough with basic Python to
begin working with libraries such as NumPy and pandas. Students who pass may
use this assessment in place of the assigned Python refresher course.

## Rules

- Complete the assessment individually.
- You may use Python's built-in `help()` function and the official Python
  documentation.
- Do not use generative AI, another person, or copied solutions.
- Edit only `answers.py`.

Attempting the fluency check does not reduce your grade. If you do not pass,
complete the assigned Python refresher by its normal deadline.

## What the assessment covers

- Variables, built-in data types, and Boolean logic
- `if`, `elif`, and `else`
- Loops, filtering, and cumulative calculations
- Strings, lists, tuples, dictionaries, and sets
- Functions, return values, and exception handling
- Basic classes, constructors, instance attributes, methods, and object state
- Processing records represented as lists of dictionaries

Inheritance and advanced object-oriented programming are not assessed.

## Setup and public examples

Install `uv`, then run:

```bash
uv sync
uv run python -m unittest discover -s tests -v
```

The public tests provide a few examples. They are not the complete grader.

## Gradescope submission

1. Complete every task in `answers.py`.
2. Run the public examples locally.
3. Open the **Python Fluency Check** assignment in Gradescope.
4. Upload `answers.py`. Do not upload the repository ZIP.
5. Review the automatic result. You may revise and resubmit before the deadline.

To pass, you must earn:

- At least 80 points on the 100-point diagnostic score
- At least 24/40 in fundamentals and control flow
- At least 21/35 in collections and data manipulation
- At least 15/25 in functions, exceptions, and classes

A passing submission receives full credit for the readiness requirement.

