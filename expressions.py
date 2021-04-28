from typing import Dict

class Expr:
    def __init__(self):
        pass

    def evaluate(self, variables: Dict[str, float]):
        pass


class Constant(Expr):
    def __init__(self, value: float):
        super().__init__()
        self.value = value

    def evaluate(self, variables: Dict[str, float]):
        return self.value

class Variable(Expr):
    def __init__(self, variable_name: str):
        super().__init__()
        self.variable_name = variable_name

    def evaluate(self, variables: Dict[str, float]):
        if self.variable_name in variables:
            return variables[self.variable_name]
        else:
            raise Exception("Variable " + self.variable_name + " was not passed a value")

class UnaryExpr(Expr):
    def __init__(self, expr: Expr):
        super().__init__()
        self.expr = expr


class Neg(UnaryExpr):
    def __init__(self, expr: Expr):
        super().__init__(expr)

    def evaluate(self, variables: Dict[str, float]):
        return (-1) * self.expr.evaluate(variables)


class BinaryExpr(Expr):
    def __init__(self, left_expr: Expr, right_expr: Expr):
        super().__init__()
        self.left_expr = left_expr
        self.right_expr = right_expr


class Plus(BinaryExpr):
    def __init__(self, left_expr: Expr, right_expr: Expr):
        super().__init__(left_expr, right_expr)

    def evaluate(self, variables: Dict[str, float]):
        return self.left_expr.evaluate(variables) + self.right_expr.evaluate(variables)


class Minus(BinaryExpr):
    def __init__(self, left_expr: Expr, right_expr: Expr):
        super().__init__(left_expr, right_expr)

    def evaluate(self, variables: Dict[str, float]):
        return self.left_expr.evaluate(variables) - self.right_expr.evaluate(variables)


class Multiply(BinaryExpr):
    def __init__(self, left_expr: Expr, right_expr: Expr):
        super().__init__(left_expr, right_expr)

    def evaluate(self, variables: Dict[str, float]):
        return self.left_expr.evaluate(variables) * self.right_expr.evaluate(variables)


class Divide(BinaryExpr):
    def __init__(self, left_expr: Expr, right_expr: Expr):
        super().__init__(left_expr, right_expr)

    def evaluate(self, variables: Dict[str, float]):
        return self.left_expr.evaluate(variables) / self.right_expr.evaluate(variables)