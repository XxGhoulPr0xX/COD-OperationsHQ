# Define los vocabularios V y W


import itertools


V = ["i", "x"]
W = ["i", "v", "c"]

# Calcula V^3 (potencia)
V_pow_3 = V+V+V

# Calcula V* (cierre de Kleene)
V_star = {""}  # Incluye la cadena vacía
for i in range(1, 4):  # Supongamos hasta longitud 3
    for combo in itertools.product(V, repeat=i):
        V_star.add("".join(combo))

# Calcula VW (concatenación)
VW = set()
for v_str in V_star:
    for w_str in W:
        VW.add(v_str + w_str)

# Imprime los resultados
print("V^3:", V_pow_3)
print("V*:", V_star)
print("VW:", VW)
