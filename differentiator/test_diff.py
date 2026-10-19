from polynomial_diff import evaluate, diff

poly_1 = ["+", ["*", 3, "x"], 5] # 3x+5
poly_2 = ["-", ["^", "x", 3], 7] # x^3-7
poly_3 = ["+", ["^", "x", 4], ["+", ["*", "x", 2], 1]] # x^4 + 2x + 1

def test_evaluate():
    for x in [-2, -1, 0, 1, 2, 3]:
        assert evaluate(poly_1, x) == 3*x + 5
        assert evaluate(poly_2, x) == x**3 - 7
        assert evaluate(poly_3, x) == x**4 + 2*x + 1


def test_diff():
    diff_1 = diff(poly_1) # 3
    diff_2 = diff(poly_2) # 3x^2
    diff_3 = diff(poly_3) # 4x^3 + 2

    for x in [-2, -1, 0, 1, 2, 3]:
        assert evaluate(diff_1, x) == 3
        assert evaluate(diff_2, x) == 3 * x**2
        assert evaluate(diff_3, x) == 4 * x**3 + 2


def test_product_rule():
    poly = ["*", ["+", "x", 1], ["+", "x", 2]] # (x+1)(x+2) = x^2 + 3x +2
    derivative = diff(poly) # 2x+3

    for x in [-2, -1, 0, 1, 2]:
        assert evaluate(derivative, x) == 2*x + 3

def test_chain_rule():
    poly = ["^", ["+", "x", 1], 3] # (x+1)^3 = x^3 + 3x^2 + 3x + 1
    derivative = diff(poly) # 3x^2 + 6x + 3

    for x in [-2, -1, 0, 1, 2]:
        assert evaluate(derivative, x) == 3* x**2 + 6*x + 3