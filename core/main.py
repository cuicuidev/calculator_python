from . import token as t
from . import shunting_alg as sa
from . import node

def calculator(input_string) -> None:
    infix_tokens = t.tokenize(input_string)
    postfix_tokens = sa.shunting_yard(infix_tokens)
    root = node.Node.from_postfix(postfix_tokens)
    return root.evaluate()