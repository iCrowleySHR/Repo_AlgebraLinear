# 🛰️ Projeto: Análise de Deslocamento de Drone com Vetores

Este projeto utiliza Python para calcular e visualizar o deslocamento de um drone
entre três pontos no plano cartesiano, analisando:

- Vetores de deslocamento
- Distâncias percorridas
- Ângulo entre os vetores
- Visualização gráfica da trajetória

---

## 📦 Requisitos

Certifique-se de ter o Python 3 instalado.

Instale as dependências necessárias:

pip install numpy matplotlib

---

## ▶️ Como executar

Salve o código em um arquivo, por exemplo:

app.py

Execute com:

python app.py

---

## 📊 O que o código faz

1. Define três pontos no plano:
   - A (0, 0)
   - B (5, 10)
   - C (10, 5)

2. Calcula:
   - Vetor AB
   - Vetor BC
   - Distância entre A e B
   - Distância entre B e C
   - Ângulo entre os vetores AB e BC

3. Gera um gráfico contendo:
   - Trajetória do drone
   - Vetores com setas
   - Identificação dos pontos
   - Informações de distância e ângulo no título

---

## 🧮 Fórmulas Utilizadas

Distância entre dois pontos:
||v|| = sqrt(x² + y²)

Produto escalar:
A · B = |A||B| cos(θ)

Ângulo:
θ = arccos( (A · B) / (|A||B|) )

---

## 📁 Estrutura Esperada

.
├── app.py
└── README.md

---

## 🎯 Resultado Esperado

O programa exibirá um gráfico mostrando:

- A trajetória A → B → C
- Os vetores de deslocamento
- As distâncias calculadas
- O ângulo entre os vetores

---

## 📚 Tecnologias Utilizadas

- Python 3
- NumPy
- Matplotlib

---

## 👨‍💻 Autor

Projeto para estudo de vetores, geometria analítica e visualização de dados.
