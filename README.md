# unicode-textbox

Reads text from `stdin` and outputs it wrapped in an Unicode text box.

## Requirements:

* python 3 only

## Usage

```
fortune | ./box.py
```

## Example output

```
┌──────────────────────────────────────────────────────┐
│ Clarity                                              │
│                                                      │
│ The origin of the world is its mother;               │
│ Understand the mother, and you understand the child; │
│ Embrace the child, and you embrace the mother,       │
│ Who will not perish when you die.                    │
│ Reserve your judgments and words                     │
│ And you maintain your influence;                     │
│ Speak your mind and take positions                   │
│ And nothing will save you.                           │
│ As observing detail is clarity,                      │
│ So maintaining flexibility is strength;              │
│ Use the light but shed no light,                     │
│ So that you do yourself no harm,                     │
│ But embrace clarity.                                 │
│                 -- Lao Tse, "Tao Te Ching"           │
└──────────────────────────────────────────────────────┘
```

## Tips

* You can put it on your `$PATH`, rename it to `box` and simple pipe to `box`,
`| box`
