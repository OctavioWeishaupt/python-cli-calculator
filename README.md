# Python CLI Calculator

A command-line calculator written in Python, with a persistent
calculation history that survives between sessions.

## About

This is a learning project from my first stage as a self-taught backend
developer. It was built ticket by ticket (one small task at a time),
using feature branches, semantic commits and pull requests, to practice
not only Python but also the engineering workflow around it: separation
of responsibilities, validation at the boundaries and documented
decisions.

## Features

- Five operations: addition, subtraction, multiplication, division and
  power.
- Input validation: the program asks again until a valid number is
  typed. Both `3.5` and `3,5` are accepted as decimals.
- Clear errors for division by zero, results too large to represent and
  non-real results.
- Persistent history saved in a text file.
- Clear the history with a yes/no confirmation.
- Colored output: titles in cyan, errors in red, results and
  confirmations in green, warnings in yellow.
- Clean exit with option `0` (or `Ctrl+C`).

## Requirements

- Python **3.12+** (the code uses `match` and f-strings that reuse the
  same quote type inside the expression).
- No external dependencies.

## How to run

```bash
git clone https://github.com/OctavioWeishaupt/python-cli-calculator.git
cd python-cli-calculator
python main.py
```

Run it from the project root: `history.txt` is created in the folder
the program is started from. The interface is in Portuguese.

## Usage

| Option | Menu label | Action |
|--------|------------|--------|
| 0 | Sair | Exit the program |
| 1 | Somar | Addition |
| 2 | Subtrair | Subtraction |
| 3 | Multiplicar | Multiplication |
| 4 | Dividir | Division |
| 5 | Potência | Power |
| 6 | Ver histórico | Show the history |
| 7 | Limpar histórico | Clear the history (asks for confirmation) |

Decimals can be typed with a dot or a comma (`3.5` or `3,5`). To leave
the program, choose option `0` or press `Ctrl+C`.

Example of a calculation and of the history:

```
3.5 + 2 = 5.5
```

```
--------------------------------------------------
                    HISTÓRICO:
--------------------------------------------------
1. 3.5 + 2 = 5.5
2. 10 / 4 = 2.5
--------------------------------------------------
```

## Project structure

```
python-cli-calculator/
├── main.py              # entry point: main loop and clean exit
├── calculator/
│   ├── operations.py    # the math functions, with no input or output
│   ├── inputs.py        # validated user input (numbers, yes/no)
│   ├── ui.py            # display helpers: lines, titles, number
│   │                    # formatting and colors
│   ├── menu.py          # menu, dispatching and operation flow
│   └── history.py       # persistence in history.txt
├── history.txt          # created at runtime (git-ignored)
└── README.md
```

## Design decisions

- **Separation of responsibilities.** Math lives in `operations.py`,
  input validation in `inputs.py`, display in `ui.py` and storage in
  `history.py`. Functions that build data or text return it, and the
  caller decides when to print.
- **Raw numbers are stored, formatting happens on display.** The history
  file keeps full precision; `format_number` rounds to 6 decimal places
  only when showing a value.
- **The file is the single source of truth.** There is no in-memory
  copy of the history: each read parses `history.txt`, so there is
  nothing to keep in sync.
- **A hand-edited file does not crash the program.** Lines that are
  blank, incomplete or with invalid values are skipped when reading.
- **Safe default for a destructive action.** At the clear confirmation,
  an empty answer is invalid and the question is asked again.
- **Colors are centralized.** All ANSI codes live in `ui.py`; other
  modules only call its helpers.

### History file format

One calculation per line, fields separated by `;`:

```
3.5;+;2.0;5.5
10.0;/;4.0;2.5
```

## Testing

Each feature was verified with manual test tables covering valid input,
invalid input and edge cases. Automated tests are not part of the
project yet.

## Known limitations and next steps

- Very large and very small results are shown in plain notation instead
  of scientific notation ([#1](../../issues/1)). Values below `5e-7`
  are displayed as `0` because of the 6-decimal rounding.
- Per-operation error messages cannot be customized yet
  ([#2](../../issues/2)).
- If the last line of `history.txt` is edited by hand and loses its
  trailing newline, the next saved calculation is glued to it and
  ignored on read.
- Invalid history lines are skipped silently, without a log.
- Automated tests.
