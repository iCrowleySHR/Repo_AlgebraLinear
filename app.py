import numpy as np
import matplotlib.pyplot as plt

# Definir pontos
A = np.array([0, 0])
B = np.array([5, 10])
C = np.array([10, 5])

# Calcular vetores de deslocamento
AB = B - A
BC = C - B

# Calcular distâncias
dist_AB = np.linalg.norm(AB)
dist_BC = np.linalg.norm(BC)

# Calcular angulo entre os vetores
cos_theta = np.dot(AB, BC) / (np.linalg.norm(AB) * np.linalg.norm(BC))
angle_rad = np.arccos(cos_theta)
angle_deg = np.degrees(angle_rad)

# Criar gráfico
plt.figure(figsize=(8,6))

# trajetória
plt.plot([A[0], B[0], C[0]],[A[1], B[1], C[1]], 'bo-', label='trajetória')

# vetores com setas
plt.quiver(A[0], A[1], AB[0], angles='xy', scale_units='xy', scale=1, color='r', label='VETOR AB')
plt.quiver(B[0], B[1], BC[0], angles='xy', scale_units='xy', scale=1, color='r', label='VETOR BC')

# anotar pontos
plt.text(A[0], A[1], 'A', fontsize=12, ha='right')
plt.text(B[0], B[1], 'B', fontsize=12, ha='right')
plt.text(C[0], C[1], 'C', fontsize=12, ha='right')

# Configurações do gráfico
plt.title(f"Deslocamento do dorne \n Dist AB: {dist_AB:.2f}, Dist BC: {dist_BC:.2f}, Ângulo {angle_deg:.2f}")
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()

