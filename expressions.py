
class Expr:
    def __init__(self):
        pass

    def evaluate(self):
        pass


class Constant(Expr):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def evaluate(self):
        return self.value


class UnaryExpr(Expr):
    def __init__(self, expr):
        super().__init__()
        self.expr = expr


class Neg(UnaryExpr):
    def __init__(self, expr):
        super().__init__(expr)

    def evaluate(self):
        return (-1) * self.expr.evaluate()


class BinaryExpr(Expr):
    def __init__(self, left_expr: Expr, right_expr: Expr):
        super().__init__()
        self.left_expr = left_expr
        self.right_expr = right_expr


class Plus(BinaryExpr):
    def __init__(self, left_expr: Expr, right_expr: Expr):
        super().__init__(left_expr, right_expr)

    def evaluate(self):
        return self.left_expr.evaluate() + self.right_expr.evaluate()


class Minus(BinaryExpr):
    def __init__(self, left_expr: Expr, right_expr: Expr):
        super().__init__(left_expr, right_expr)

    def evaluate(self):
        return self.left_expr.evaluate() - self.right_expr.evaluate()


class Multiply(BinaryExpr):
    def __init__(self, left_expr: Expr, right_expr: Expr):
        super().__init__(left_expr, right_expr)

    def evaluate(self):
        return self.left_expr.evaluate() * self.right_expr.evaluate()


class Divide(BinaryExpr):
    def __init__(self, left_expr: Expr, right_expr: Expr):
        super().__init__(left_expr, right_expr)

    def evaluate(self):
        return self.left_expr.evaluate() / self.right_expr.evaluate()