import numpy as np

# ler vetores
u = np.array(list(map(float, input("Digite os componentes de u separados por espaço: ").split())))
v = np.array(list(map(float, input("Digite os componentes de v separados por espaço: ").split())))

# produto escalar
dot_uv = np.dot(u, v)
dot_vv = np.dot(v, v)

# projeção de u em v (componente paralela)
proj_v_u = (dot_uv / dot_vv) * v

# componente perpendicular
u_perp = u - proj_v_u

print("Componente paralela (útil):", proj_v_u)
print("Componente perpendicular (erro de navegação):", u_perp)