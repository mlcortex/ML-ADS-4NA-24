import numpy as np
import pandas as pd

# Lista de valores
valores = [4, 6, 3, 4, 5, 8, 4, 2]

# Convertendo para um array NumPy para facilitar os cálculos
valores_array = np.array(valores)

# Calculando as estatísticas
valor_maximo = np.max(valores_array)
valor_minimo = np.min(valores_array)
media = np.mean(valores_array)
mediana = np.median(valores_array)
desvio_padrao = np.std(valores_array)

# Imprimindo os resultados
print("Valor máximo:", valor_maximo)
print("Valor mínimo:", valor_minimo)
print("Média aritmética:", media)
print("Mediana:", mediana)
print("Desvio padrão:", desvio_padrao)
