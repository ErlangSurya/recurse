"""
We use Abstract Syntax Tree representation for polynomial, which generalizes nicely to accomodate other functions (e.g. trigonometric functions).
For example:
3x+2 can be represented as ["+", ["*", 3, "x"], 2]
x^4 + 2x + 1 can be represented as ["+", ["^", "x", 4], ["+", ["*", "x", 2], 1]]


Some possible extensions:
- Deduce canonical form sum_{i=0}^n a_i x^i from arbitrary AST
- Support pretty print
- Support division and rational functions (ratio of two polynomials)
- Support sin and cos
"""

FUNCTIONS = ["*", "+", "-", "^"]


def diff(poly):
    if isinstance(poly, list):
        assert len(poly) == 3
        op = poly[0]
        assert op in FUNCTIONS
        if op == "*":
            return ["+", ["*", diff(poly[1]), poly[2]], ["*", poly[1], diff(poly[2])]]
        elif op == "^":
            assert isinstance(poly[2], int)
            assert poly[2] >= 0
            if poly[2] == 0:
                return 0
            else:
                return ["*", diff(poly[1]), ["*", poly[2], ["^", poly[1], poly[2] - 1]]]
        elif op in ["+", "-"]:
            return [op, diff(poly[1]), diff(poly[2])]
        else:
            raise ValueError(f"op value {op} invalid")
    elif isinstance(poly, str):
        assert poly == "x"
        return 1
    elif isinstance(poly, (int, float)):
        return 0
    raise ValueError


def evaluate(poly, x):
    if isinstance(poly, list):
        assert len(poly) == 3
        op = poly[0]
        assert op in FUNCTIONS
        if op == "*":
            return evaluate(poly[1], x) * evaluate(poly[2], x)
        elif op == "^":
            assert isinstance(poly[2], int) and poly[2] >= 0
            return (evaluate(poly[1], x))**poly[2]
        elif op == "+":
            return evaluate(poly[1], x) + evaluate(poly[2], x)
        elif op == "-":
            return evaluate(poly[1], x) - evaluate(poly[2], x)   
        else:
            raise ValueError(f"op value {op} invalid")
    elif poly == 'x':
        return x
    elif isinstance(poly, (int,float)):
        return poly
    else:
        raise ValueError(f"poly: {poly} unsupported")