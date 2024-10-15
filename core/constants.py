# PEMDAS operators
OPERATORS = "^*/+-"
BRACKETS = "()"

# PEMDAS precedence
PRECEDENCE = {
    "^": 3,
    "*": 2,
    "/": 2,
    "+": 1,
    "-": 1
}

# Operator associativity
ASSOCIATIVITY = {
    "^": "right",
    "*": "left",
    "/": "left",
    "+": "left",
    "-": "left"
}