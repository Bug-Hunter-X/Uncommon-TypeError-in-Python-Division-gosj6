# Uncommon TypeError in Python Division

This repository demonstrates an uncommon `TypeError` that can occur in Python during division operations.  The error arises when attempting to divide a number by a string, resulting in an unexpected `TypeError` instead of a more commonly anticipated `ZeroDivisionError`.

## The Bug

The `bug.py` file contains a function that attempts to handle division errors using `try-except`. However, it doesn't explicitly address the `TypeError` encountered when dividing by a string. This is an edge case often overlooked, leading to unexpected behavior or program crashes.  The script then attempts a division with a string, causing the TypeError.

## The Solution

The `bugSolution.py` file addresses this uncommon error by explicitly including a `TypeError` exception in the `try-except` block.  This ensures that the program handles this specific error gracefully, preventing unexpected crashes and providing informative error messages.

## Running the Code

To run the code, simply execute the Python scripts using a Python interpreter (Python 3.x recommended):

```bash
python bug.py
python bugSolution.py
```