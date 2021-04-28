from expressions import *

from mtoken import MToken, TokenType

class Tokenizer:
    def __init__(self, text: str):
        self.text = text

        self.current_index = 0

    def tokenize(self) -> [MToken]:
        tokens = []

        while self.current_index < len(self.text):
            c = self.text[self.current_index]

            if c.isnumeric():
                num_value = self.consume_number()
                tokens.append(MToken(TokenType.NUMBER, num_value))
            elif c == "(":
                group_str = self.consume_grouping()
                t = Tokenizer(group_str)

                tokens.append(MToken(TokenType.GROUPING, t.tokenize()))
            elif c == "+":
                tokens.append(MToken(TokenType.PLUS))
                self.current_index += 1
            elif c == "-":
                tokens.append(MToken(TokenType.MINUS))
                self.current_index += 1
            elif c == "*":
                tokens.append(MToken(TokenType.TIMES))
                self.current_index += 1
            elif c == "/":
                tokens.append(MToken(TokenType.DIVIDE))
                self.current_index += 1
            else:
                # throw out the current character
                self.current_index += 1

            # TODO this currently won't work for negative numbers, it will just become subtraction
            # try and figure out a way to get it to work

        return tokens

    def consume_number(self) -> int:
        """
        Consumes characters until a non-numeric character is reached
        :return:
        The next number in the expression
        """

        result_string = ""

        while self.current_index < len(self.text):
            c = self.text[self.current_index]

            if c.isnumeric():
                result_string += c
                self.current_index += 1
            else:
                break

        return int(result_string)


    def consume_grouping(self) -> str:
        num_unclosed_parens = 1
        result = ""

        self.current_index += 1

        for c in self.text[self.current_index:]:
            if c == "(":
                num_unclosed_parens += 1
            elif c == ")":
                num_unclosed_parens -= 1

                if num_unclosed_parens == 0:
                    break

            result += c

        self.current_index += len(result) + 1
        return result
