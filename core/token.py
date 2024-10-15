from enum import Enum
from typing import Type

from . import constants as const

class TokenType(Enum):
    INT: str = "int"
    FLOAT: str = "float"
    OPERATOR: str = "operator"
    BRACKET: str = "bracket"
    WSPACE: str = "wspace"

class Token:
    """Token class. Responsible for holding a token of type string and some metadata."""

    def __init__(self, value: str, type: TokenType) -> None:
        self.value = value
        self.type = type

    def __repr__(self) -> str:
        return self.value
    
    def __eq__(self, other: Type["Token"] | str) -> bool:
        if isinstance(other, Token):
            return self.value == other.value and self.type == other.type
        if isinstance(other, str):
            return self.value == other
        raise TypeError(f"Cannot compare type 'Token' to type '{type(other)}'")

def tokenize(string: str) -> list[Token]:
    """Takes in an algebraic expression as a string and tokenizes it. Handles some of the syntax errors that could arise."""
    tokens: list[Token] = []

    i = 0
    n_chars = len(string)

    num_buffer = []
    while i < n_chars:
        char: str = string[i]

        if char.isalpha():
            raise SyntaxError(f"Unrecognized character: {char} - ASCII<{ord(char)}>")
        
        if char.isnumeric():
            num_buffer.append(char)
            i += 1
            continue

        if char == ".":            
            if "." in num_buffer:
                raise SyntaxError("Cannot process a number with multiple dots")
            num_buffer.append(char)
            i += 1
            continue

        if len(num_buffer) != 0:
            num = "".join(num_buffer)
            if "." in num:
                tokens.append(Token(value=num, type=TokenType.FLOAT))
            else:
                tokens.append(Token(value=num, type=TokenType.INT))
            num_buffer.clear()

        if char in const.OPERATORS:
            tokens.append(Token(value=char, type=TokenType.OPERATOR))
            i += 1
            continue

        if char in const.BRACKETS:
            tokens.append(Token(value=char, type=TokenType.BRACKET))
            i += 1
            continue

        i += 1

    if len(num_buffer) != 0:
        num = "".join(num_buffer)
        if "." in num:
            tokens.append(Token(value=num, type=TokenType.FLOAT))
        else:
            tokens.append(Token(value=num, type=TokenType.INT))

    return tokens