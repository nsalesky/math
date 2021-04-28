from expressions import *
from tokenizer import Tokenizer
from express import express, group_priority

def evaluate_str(expression: str) -> float:
    tokenizer = Tokenizer(expression)
    tokens = tokenizer.tokenize()

    grouped_tokens = group_priority(tokens)

    expr = express(grouped_tokens)

    return expr.evaluate()


if __name__ == "__main__":
    test_str = "(9+ 5)* 7"

    print(evaluate_str(test_str))