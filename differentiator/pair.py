from polynomial_diff import *


poly_1 = ["+", ["*", 3, "x"], 5] # 3x+5
poly_2 = ["-", ["^", "x", 3], 7] # x^3-7
poly_3 = ["+", ["^", "x", 4], ["+", ["*", "x", 2], 1]] # x^4 + 2x + 1
poly_4 = ["^", ["+", "x", 2], 3]

def pretty_print_ast(poly):
    if isinstance(poly, list):
        assert len(poly) == 3
        op, p1, p2 = poly
        return pretty_print_ast(p1) + op + pretty_print_ast(p2)
    else:
        return str(poly)
    # elif isinstance(poly, (int,float)):
    #     return str(poly)

# print(pretty_print_ast(poly_1))
# print(pretty_print_ast(poly_2))
# print(pretty_print_ast(poly_3))

def padding(l1, l2):
    n = max(len(l1), len(l2))
    l1_pad = [l1[i] if i<len(l1) else 0 for i in range(n)]
    l2_pad = [l2[i] if i<len(l2) else 0 for i in range(n)]
    return l1_pad, l2_pad

l1 = [1,2,3]
l2 = [4,2]
l3 = [7,6,4,2,2,4]

def canonical_op(op, p1_can, p2_can):
    """
    p1, p2 are in canonical form, or p2 is a number when op is ^
    """
    p1_pad, p2_pad = padding(p1_can, p2_can)
    if op == "+":    
        return [x+y for x,y in zip(p1_pad, p2_pad)]
    elif op == "-":
        return [x-y for x,y in zip(p1_pad, p2_pad)]
    elif op == "*":
        n = len(p1_pad)
        result = [0 for _ in range(2*n)]
        for i in range(n):
            for j in range(n):
                result[i+j] += p1_pad[i] * p2_pad[j]
        return result
    elif op == "^":
        # In this case p1_can is the base, p2 HAS TO BE A NUMBER
        assert isinstance(p2_can, list)
        assert len(p2_can) == 1
        assert isinstance(p2_can[0], int)
        power = p2_can[0]
        if power == 0:
            return [1]
        elif power == 1:
            return p1_can
        else:
            # p1_can * (p1_can ** (p2-1))
            smaller_case = canonical_op("^", p1_can, [power-1])
            return canonical_op("*", p1_can,  smaller_case)
    else:
        raise ValueError(f"{op} not recognized")
            


def ast_to_canonical(poly):
    """
    In the canonical form representation, let's write 
    sum_{i=0}^n a_i x^i  -> [a_0, a_1, a_2,...,a_n]
    """
    if isinstance(poly, list):
        assert len(poly)==3
        op, p1, p2 = poly
        p1_can = ast_to_canonical(p1)
        p2_can = ast_to_canonical(p2)
        # need to make sure they're the same length
        return canonical_op(op, p1_can, p2_can)
    elif isinstance(poly, str):
        assert poly == "x"
        return [0, 1]
    elif isinstance(poly, (int,float)):
        return [poly]
    else:
        raise ValueError(f"{poly} not recognized")

print("First case")
print(ast_to_canonical(poly_1))

print("Second case")
print(ast_to_canonical(poly_2))

print("Third case")
print(ast_to_canonical(poly_3))

print("Fourth case")
print(ast_to_canonical(poly_4))