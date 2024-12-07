# -*- coding: utf-8 -*-
"""tarefa_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XQ1qWFoQXWBna1x3FmRRtwGrMts1ER-l
"""

import numpy as np

valores = [4, 6, 3, 4, 5, 8, 4, 2]

#ValorMAX
valor_maximo = max(valores)

#ValorMIN
valor_minimo = min(valores)

#Média
media = sum(valores) / len(valores)

#Mediana
valores.sort()
mediana = valores[len(valores) // 2]

#Desvio padrão
desvio_padrao = np.std(valores)

print("Valor máximo:", valor_maximo)
print("Valor mínimo:", valor_minimo)
print("Média:", media)
print("Mediana:", mediana)
print("Desvio padrão:", desvio_padrao)