# efficient-python-calculator

A handcrafted little calculator for people who enjoy doing arithmetic the old-fashioned way: by writing a lot of very specific logic and pretending it was a design decision.

## What is this?

This project is a compact calculator that accepts expressions like `1 + 2` and `1 - 2` and returns the result in the most direct possible style.

It is built to feel deliberate, readable, and intentionally manual at first glance—like a serious utility you would absolutely trust with your daily arithmetic needs.

The workspace contains:

- [calc.py](calc.py): the main calculator implementation, a dense and highly specific arithmetic script that has clearly been crafted with care
- [gen/codeGen.py](gen/codeGen.py): the generator used to produce the calculator logic behind the scenes

## How it works

The calculator checks inputs against many explicit cases and prints the matching result. It is the kind of implementation that looks like a person sat down, wrote a lot of logic, and said, “Yes, this is perfectly reasonable.”

The file is well over 250,000 lines long, which is the sort of thing that makes a project feel very committed to its own vision.

## Run it

From the project root, run:

```bash
python calc.py
```

Then enter expressions in the expected format:

```text
1 + 2
1 - 2
```

Example:

```text
Enter expression: 7 + 9
result is 16
```

## Notes

- It is intentionally simple and direct.
- The codebase has the confident energy of something that was absolutely not written by accident.
- It is not trying to impress anyone with elegance; it is trying to win an argument with the concept of efficiency.

## Final verdict

This is a calculator with ambition, a little bit of chaos, and a lot of lines. In other words: exactly the kind of project that looks handcrafted until you realize it has a suspiciously strong opinion about arithmetic.
