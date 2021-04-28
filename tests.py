from expressions import *
from tokenizer import *
# import token

import unittest


class TestExpressions(unittest.TestCase):
    def setUp(self):
        self.one = Constant(1)
        self.two = Constant(2)
        self.three = Constant(3)

        self.neg_two = Neg(self.two)

        self.add_one_two = Plus(self.one, self.two)
        self.two_minus_three = Minus(self.two, self.three)
        self.two_times_three = Multiply(self.two, self.three)
        self.two_div_two = Divide(self.two, self.two)

    def test_constant(self):
        self.assertEqual(self.one.evaluate(), 1)
        self.assertEqual(self.two.evaluate(), 2)

    def test_neg(self):
        self.assertEqual(self.neg_two.evaluate(), -2)

    def test_plus(self):
        self.assertEqual(self.add_one_two.evaluate(), 3)

    def test_minus(self):
        self.assertEqual(self.two_minus_three.evaluate(), -1)

    def test_multiply(self):
        self.assertEqual(self.two_times_three.evaluate(), 6)

    def test_divide(self):
        self.assertEqual(self.two_div_two.evaluate(), 1)


class TestTokenizer(unittest.TestCase):
    def setUp(self):
        pass

    def test_tokenize(self):
        t1 = Tokenizer("1234")
        t2 = Tokenizer("123 + 321")
        t3 = Tokenizer("43 * (1 + 2) - 4")
        t4 = Tokenizer("1 + (((2) 3) 4) 5")

        self.assertEqual(t1.tokenize(), [MToken(TokenType.NUMBER, 1234)])

        self.assertEqual(t2.tokenize(), [MToken(TokenType.NUMBER, 123),
                                          MToken(TokenType.PLUS),
                                          MToken(TokenType.NUMBER, 321)])
        self.assertEqual(t3.tokenize(), [MToken(TokenType.NUMBER, 43),
                                         MToken(TokenType.TIMES),
                                         MToken(TokenType.GROUPING,
                                                [MToken(TokenType.NUMBER, 1),
                                                 MToken(TokenType.PLUS),
                                                 MToken(TokenType.NUMBER, 2)]),
                                         MToken(TokenType.MINUS),
                                         MToken(TokenType.NUMBER, 4)])
        self.assertEqual(t4.tokenize(), [MToken(TokenType.NUMBER, 1),
                                         MToken(TokenType.PLUS),
                                         MToken(TokenType.GROUPING,
                                                [MToken(TokenType.GROUPING,
                                                    [MToken(TokenType.GROUPING,
                                                            [MToken(TokenType.NUMBER, 2)]),
                                                     MToken(TokenType.NUMBER, 3)]),
                                                 MToken(TokenType.NUMBER, 4)]),
                                         MToken(TokenType.NUMBER, 5)])


    def test_consume_number(self):
        t1 = Tokenizer("1234 + 5 - 7")
        t2 = Tokenizer("123 456")

        self.assertEqual(t1.current_index, 0)
        self.assertEqual(t1.consume_number(), 1234)
        self.assertEqual(t1.current_index, 4)

        self.assertEqual(t2.current_index, 0)
        self.assertEqual(t2.consume_number(), 123)
        self.assertEqual(t2.current_index, 3)

    def test_consume_grouping(self):
        t1 = Tokenizer("(1234) + 5")
        t2 = Tokenizer("(5 + (4 * 2 - ) / ((1 - 2) + 3))))))")

        self.assertEqual(t1.current_index, 0)
        # self.assertEqual(t1.consume_grouping(), [MToken(TokenType.NUMBER, 1234)])
        self.assertEqual(t1.consume_grouping(), "1234")
        self.assertEqual(t1.current_index, 6)

        self.assertEqual(t2.current_index, 0)
        self.assertEqual(t2.consume_grouping(), "5 + (4 * 2 - ) / ((1 - 2) + 3)")
        self.assertEqual(t2.current_index, 32)
