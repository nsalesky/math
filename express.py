from expressions import *
from mtoken import *


# This first attempt won't follow GEMA, it will just naively express
# the tokens as an expression

def express(tokens: [MToken]) -> Expr:
    current_index = 0

    left_expr = None

    if len(tokens) == 0:
        raise Exception("Cannot express an empty list")

    while current_index < len(tokens):
        tok = tokens[current_index]

        if tok.token_type == TokenType.NUMBER:
            left_expr = express_token(tok)

            current_index += 1
        elif tok.token_type == TokenType.GROUPING:
            left_expr = express_token(tok)

            current_index += 1
        elif tok.token_type == TokenType.VARIABLE:
            left_expr = express_token(tok)

            current_index += 1
        elif tok.token_type == TokenType.PLUS:
            right_expr = express_token(tokens[current_index + 1])
            left_expr = Plus(left_expr, right_expr)

            current_index += 2
        elif tok.token_type == TokenType.MINUS:
            right_expr = express_token(tokens[current_index + 1])
            left_expr = Minus(left_expr, right_expr)

            current_index += 2
        elif tok.token_type == TokenType.TIMES:
            right_expr = express_token(tokens[current_index + 1])
            left_expr = Multiply(left_expr, right_expr)

            current_index += 2
        elif tok.token_type == TokenType.DIVIDE:
            right_expr = express_token(tokens[current_index + 1])
            left_expr = Divide(left_expr, right_expr)

            current_index += 2

    return left_expr


def express_token(token: MToken) -> Expr:
    if token.token_type == TokenType.NUMBER:
        return Constant(token.value)
    elif token.token_type == TokenType.GROUPING:
        return express(token.value)
    elif token.token_type == TokenType.VARIABLE:
        return Variable(token.value)
    else:
        raise Exception("Can't express an individual token of type" + str(token.token_type))


def group_priority(tokens: [MToken]) -> [MToken]:
    """Adds grouping around multiplication and division from left to right to prioritize them for GEMA"""

    current_index = 0

    result_tokens = []

    while current_index < len(tokens):
        tok = tokens[current_index]

        if tok.token_type == TokenType.TIMES or tok.token_type == TokenType.DIVIDE:
            token_before = result_tokens[len(result_tokens) - 1]
            result_tokens.remove(token_before)

            group = MToken(TokenType.GROUPING,
                           [token_before,
                            tok,
                            tokens[current_index + 1]])
            result_tokens.append(group)

            current_index += 2
        else:
            result_tokens.append(tok)

            current_index += 1

    return result_tokens
