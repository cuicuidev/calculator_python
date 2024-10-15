from . import constants as const
from . import token as t

def shunting_yard(tokens: list[t.Token]) -> list[t.Token]:
    """Shunting yard algorithm implementation with some error handling for syntax"""
    output: list[t.Token] = []
    operator_stack: list[t.Token] = []

    for token in tokens:
        if token.type in {t.TokenType.INT, t.TokenType.FLOAT}:
            output.append(token)
        elif token.type == t.TokenType.OPERATOR:
            while (operator_stack and 
                   operator_stack[-1].type == t.TokenType.OPERATOR and 
                   ((const.ASSOCIATIVITY[token.value] == "left" and 
                     const.PRECEDENCE[token.value] <= const.PRECEDENCE[operator_stack[-1].value]) or
                    (const.ASSOCIATIVITY[token.value] == "right" and 
                     const.PRECEDENCE[token.value] < const.PRECEDENCE[operator_stack[-1].value]))):
                output.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == "(":
            operator_stack.append(token)
        elif token == ")":
            while operator_stack and operator_stack[-1] != "(":
                output.append(operator_stack.pop())
            operator_stack.pop()

    while operator_stack:
        top_token = operator_stack.pop()
        if top_token == "(":
            raise SyntaxError("Unmatched opening parenthesis '(' encountered.")
        output.append(top_token)

    return output