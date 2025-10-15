import math

eta1 = 35     
eta2 = 30     
N1 = 350  
N2 = 320  
V_star = 800  
S = 10  
Nkom = 12

eta = eta1 + eta2

N = N1 + N2

V = N * math.log2(eta)

D = (eta1 / 2) * (N2 / eta2)
L = 1 / D

I = L * V

T = V / (S * L)

lam = V_star * L

B = (V_star ** 2) / (3000 * lam)

F = Nkom / N1  

print(f"η1 (оператори): {eta1}")
print(f"η2 (операнди): {eta2}")
print(f"η (словник): {eta}")
print(f"N1 (кількість операторів): {N1}")
print(f"N2 (кількість операндів): {N2}")
print(f"N (довжина): {N}")
print(f"V (обсяг): {V:.3f}")
print(f"D (складність): {D:.3f}")
print(f"L (рівень якості програмування): {L:.6f}")
print(f"I (інтелектуальний зміст): {I:.3f}")
print(f"T (час програмування, сек): {T:.3f}")
print(f"λ (рівень мови програмування): {lam:.3f}")
print(f"B (кількість помилок): {B:.3f}")
print(f"F (рівень коментованості): {F:.6f}")