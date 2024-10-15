from . import token as t

class MalformedNode(Exception):
    pass

class Node:
    """Node class for a binary tree"""
    def __init__(self, token: t.Token, left: "Node" = None, right: "Node" = None) -> None:
        self.token = token
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.token}, left={self.left}, right={self.right})"
    
    def evaluate(self) -> float:
        if self.token.type == t.TokenType.INT:
            return int(self.token.value)
        elif self.token.type == t.TokenType.FLOAT:
            return float(self.token.value)

        if self.left:
            left_value = self.left.evaluate()
        else:
            raise MalformedNode(f"The node {self} contains a token of type {self.token.type} and lacks a Node on the left.")
        
        if self.right:
            right_value = self.right.evaluate()
        else:
            raise MalformedNode(f"The node {self} contains a token of type {self.token.type} and lacks a Node on the right.")

        if self.token == "+":
            return left_value + right_value
        elif self.token == "-":
            return left_value - right_value
        elif self.token == "*":
            return left_value * right_value
        elif self.token == "/":
            if right_value == 0:
                raise ZeroDivisionError("Division by zero is undefined.")
            return left_value / right_value
        elif self.token == "^":
            return left_value ** right_value
        else:
            raise ValueError(f"Unknown operator: {self.token.value}")
        
    @classmethod
    def from_postfix(cls, tokens: list[t.Token]) -> "Node":
        stack = []
        
        for token in tokens:
            if token.type in {t.TokenType.INT, t.TokenType.FLOAT}:
                stack.append(Node(token=token))
            elif token.type == t.TokenType.OPERATOR:
                right_node = stack.pop()
                left_node = stack.pop()
                
                operator_node = Node(token=token, left=left_node, right=right_node)
                
                stack.append(operator_node)
            else:
                raise ValueError(f"Unsupported token type: {token.type}")
        
        if len(stack) != 1:
            raise ValueError("The provided postfix expression is invalid.")
        
        return stack.pop()