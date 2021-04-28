from enum import Enum
from functools import total_ordering
from expressions import *

class TokenType(Enum):
    NUMBER = 1
    PLUS = 2
    MINUS = 3
    TIMES = 4
    DIVIDE = 5
    NEG = 6
    GROUPING = 7

@total_ordering
class MToken:
    def __init__(self, token_type: TokenType, value=None):
        self.token_type = token_type
        self.value = value

    def __eq__(self, other):
        return ((self.token_type, self.value) == (other.token_type, other.value))

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return (self.token_type < other.token_type)