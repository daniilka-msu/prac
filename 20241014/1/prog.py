from fractions import Fraction

def evaluate_polynomial(coefficients, x):
    result = Fraction(0)
    for degree, coeff in enumerate(coefficients):
        result += coeff * (x ** degree)
    return result

def is_solution(s, w, degree_A, coeffs_A, degree_B, coeffs_B):
    s = Fraction(s)
    w = Fraction(w)
    A_s = evaluate_polynomial(coeffs_A, s)
    B_s = evaluate_polynomial(coeffs_B, s)
    if B_s != 0:
        return A_s * 1 == B_s * w
    else:
        return False

input_data = input().strip()
data = input_data.split(", ")

s = data[0]
w = data[1]
degree_A = int(data[2])
coeffs_A = [Fraction(data[i]) for i in range(3, 3 + degree_A + 1)]
degree_B = int(data[3 + degree_A + 1])
coeffs_B = [Fraction(data[i]) for i in range(4 + degree_A + 1, len(data))]

result = is_solution(s, w, degree_A, coeffs_A, degree_B, coeffs_B)
print(result)

