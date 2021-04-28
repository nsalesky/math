from expressions import *
from tokenizer import Tokenizer
from express import express, group_priority

from typing import Dict

def evaluate_str(expression: str, variables: Dict[str, float]) -> float:
    tokenizer = Tokenizer(expression)
    tokens = tokenizer.tokenize()

    grouped_tokens = group_priority(tokens)

    expr = express(grouped_tokens)

    return expr.evaluate(variables)


if __name__ == "__main__":
    test_str = "x - (1 + x) * 3"

    my_variables = {
        "x" : 4
    }

    print(evaluate_str(test_str, my_variables))
