import numpy as np
import matplotlib.pyplot as plt

# captura dos valores do vetor u
print("Digite os valores do vetor u:")
u1 = float(input("u1 = "))
u2 = float(input("u2 = "))

# captura dos valores do vetor v
print("Digite os valores do vetor v:")
v1 = float(input("v1 = "))
v2 = float(input("v2 = "))

# cria vetores
u = np.array([u1, u2])
v = np.array([v1, v2])

# produto escalar
produto = np.dot(u,v)

def graphic():
    
    plt.figure()

    # vetor u
    plt.quiver(0,0, u[0], u[1], angles='xy', scale_units='xy')

    # vetor v
    plt.quiver(0,0, v[0], v[1], angles='xy', scale_units='xy')

    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Vetores u e v - Verificação de ortogonalidade")
    plt.show()

# verificação de ortogonalidade6
if produto == 0:
    print("Movimento correto")

if produto > 0:
    print("Movimento perpendicular: risco de colisão")

if produto < 0:
    print("Movmento invertido: ERRO")

graphic()


