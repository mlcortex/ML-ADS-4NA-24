# Equipe Cancer 3

## Equipe:
- Jadson Camilo - 01526263
- João Pedro Almeida de Albuquerque - 01758390
- Gean Carlos Silva Colares - 01618752
- Gabriel Henrique Lapa - 01616281

# Cancer 3 - Análises pertinentes a identificação de tumores
Análises necessárias para identificação de risco de tumores

# Identificação de tumores benignos ou malignos
Neste projeto realizamos análises em um DataSet que nos fornecia dados a respeito de diferentes tipos de câncer. Neste dataSet realizamos diversos processos tais como: 

- Normalização
- Treinamento e avaliação com KNN
- Cross validation com K FOLD
- Clusterização 
- Análise de caracteristicas que ajudam a identificar se um tumor é maligno ou benigno

## Base de dados
A base de dados escolhida foi a: load_breast_cancer 

## Modelo/Alg.

- Pré-processamento dos Dados utilizando MinMaxScaler da scikit-learn
    - Objetivo: padronizar a escala dos atributos para melhorar a performance de algoritmos sensíveis a magnitudes como o KNN.

- Classificação Supervisionada com modelos preditivos, sendo eles: 

    - KNN (K-Nearest Neighbors)
        - Objetivo: Algoritmo baseado em instâncias que classifica amostras com base nas classes dos vizinhos mais próximos no espaço de atributos. Para este algoritmo foram utilizados dois valores: 
            - k=3: Utiliza os 3 vizinhos mais próximos para a classificação.
            - k=5: Utiliza os 5 vizinhos mais próximos para a classificação.

    - K-Fold Cross-Validation
        - Objetivo: Validar o desempenho do KNN com maior confiabilidade.
        - Utilização no projeto: Divisão do conjunto de dados em k=10k=10 subconjuntos (folds), com validação cruzada para calcular médias e desvios padrão das acurácias.
    
    - Agrupamento Não Supervisionado:
        - Algoritmo utilizado: K-Means
        - Objetivo: Descobrir padrões nos dados sem considerar as classes originais e comparar os clusters com as classes reais.
        - Utilização no projeto: Algoritmo de agrupamento iterativo que divide os dados em kk clusters (k=4 neste caso).
    
    - Análise de Correlação
        - Algoritmo utilizado: Correlação de Pearson
        - Objetivo: Entender o impacto de cada característica na classificação e explorar possíveis redundâncias ou relações entre as variáveis.

## Objetivos
    - Classificação (KNN): Avaliar o desempenho preditivo, identificando a melhor configuração de k.
    - Clustering (K-Means): Explorou a possibilidade de separar dados sem supervisão, comparando com as classes reais.
    - Análise de Correlação: Identificou variáveis altamente correlacionadas com a classe, indicando quais atributos são mais relevantes na distinção de tumores.

## Etapas de modelagem
- Compreensão do Problema
    * Objetivo: Identificar padrões nos dados para prever a classe do câncer (maligno ou benigno).
    * Tipo de Problema: Problema de classificação supervisionada (para KNN) e agrupamento não supervisionado (para K-Means).
    * Objetivo do KNN: Classificar tumores com base nas características do tumor.
    * Objetivo do K-Means: Agrupar os dados em clusters sem utilizar a variável de classe, identificando possíveis padrões naturais.

- Carregamento e Pré-processamento dos Dados
    * Importação dos Dados: Utilizamos o Breast Cancer Dataset do scikit-learn (ou uma versão similar carregada diretamente de uma URL).
    * Exploração Inicial dos Dados: Foi verificado as características do conjunto de dados como dimensões, tipos de dados, valores ausentes.Também foi realizado o ajuste e limpeza de dados,  removendo valores ausentes ou categóricos irrelevantes.
    * Normalização dos Dados: Como muitas variáveis podem ter diferentes escalas como por exemplo: áreas e perímetros de células. Foi aplicado a normalização MinMaxScaler, que reescala as variáveis para o intervalo [0,1][0,1], tornando os dados mais adequados para algoritmos como KNN e K-Means.
    * Separação de Variáveis: X (variáveis independentes): Contém todas as colunas (exceto a coluna classe). y (variável dependente): A coluna classe (benigno ou maligno), que será o alvo da classificação.

- Treinamento do Modelo
    * K-Nearest Neighbors (KNN):
        * Objetivo: Classificar o tumor como benigno ou maligno com base nas características do tumor.
        * Algoritmo: O KNN faz isso comparando as amostras com as de seus vizinhos mais próximos, usando a distância Euclidiana.
        * Configurações de K: Treinamos o modelo com diferentes valores de k (número de vizinhos) para verificar qual valor resulta no melhor desempenho que no caso foi: k=3  e k=5.
        * Divisão de Dados: A divisão dos dados foi feita em conjuntos de treinamento e teste, utilizando uma proporção de 70% para treinamento e 30% para teste.
        * Avaliação: A acurácia foi calculada com a função accuracy_score.
    
    * K-Fold Cross-Validation:
        * Objetivo: Validar a robustez do modelo KNN. O conjunto de dados foi dividido em 10 folds (subconjuntos) e o modelo foi treinado e avaliado em cada um desses subconjuntos.
        * Avaliação: Média e desvio padrão das acurácias foram calculados para validar a confiabilidade do modelo.
    
    * K-Means (Agrupamento):
        * Objetivo: Identificar clusters sem usar a variável classe para rotular os dados.
        * Algoritmo: O K-Means tenta dividir os dados em 4 clusters e ajustar os centróides dos clusters até convergir.
        * Inércia: A inércia do modelo foi analisada, que mede a soma das distâncias quadradas entre os pontos e os seus respectivos centróides.

- Avaliação dos Modelos
    * KNN (Acurácia): A performance foi avaliada com base na acurácia que basicamente é a quantidade de previsões corretas dividida pelo número total de amostras.
    * K-Fold Cross-Validation: Uma avaliação mais robusta da acurácia foi realizada usando validação cruzada, que reduz o risco de sobreajuste.
    * K-Means: Para o K-Means, a inércia foi utilizada para avaliar o quão bem os dados foram agrupados. Além disso, a distribuição dos clusters foi comparada com as classes reais.

- Análise de Resultados

    * KNN: 
        * Foi analisado os resultados das diferentes configurações de k no caso k=3 e k=5. Para pudessemos verificar qual valor de k obteve a melhor acurácia no conjunto de teste.
        * Comparação de Desempenho: Comparação da acurácia entre os diferentes valores de kk e os diferentes valores de random_state.

    * K-MEANS:
        * Verificamos como os clusters gerados pelo K-Means se compararam com as classes reais sendo elas benigno e maligno.
        * Comparação de Distribuição: A distribuição dos clusters foi comparada com a coluna classe para verificar se os clusters gerados são relevantes.

    * Correlação de Pearson:
        * Foi calculada a correlação entre as variáveis e a classe para identificar as características mais relevantes na classificação de tumores.

- Conclusões
    * Desempenho do KNN: Identificação de qual configuração de kk oferece o melhor desempenho.
    * Análise do K-Means: Verificação de como o K-Means agrupa os dados e sua relação com as classes reais.
    * Correlação das Variáveis: Identificação de variáveis mais fortes e úteis para a classificação.

