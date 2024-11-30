# Equipe "Predictus"

## Equipe (max 4 pessoas):
- Bruno Vinícius Melo da Fonseca - 01603003
- Matheus Augusto de Moura - 01586638
- Weydson Roberval da Silva Rodrigues - 01603053



# Nome projeto
 Safe Athlete Predictus

# Tema
O projeto visa prever a probabilidade de lesões em jogadores de esportes com base em variáveis físicas, históricos de lesões e características de treinamento. O objetivo é criar um modelo preditivo para ajudar treinadores e equipes médicas a identificar atletas em risco de lesão, ajustando treinos e planos de recuperação de forma personalizada.

# Base de Dados
A base de dados utilizada contém informações sobre os jogadores, incluindo:

- Idade: A idade do jogador (em anos), que pode influenciar o risco de lesão devido ao desgaste físico com o tempo.0

- Peso (kg): O peso corporal do jogador, que afeta o desempenho físico e pode influenciar o risco de lesões em atividades de alto impacto.

- Altura (cm): A altura do jogador, que pode impactar sua aptidão física para certos esportes ou posições.

- Lesões Anteriores: Indica se o jogador teve lesões no passado (binário: 1 para sim, 0 para não). Jogadores com histórico de lesões podem ter maior risco de sofrer novas.

- Intensidade do Treino (1-5): Avaliação da intensidade do treino do jogador, onde 1 é treino leve e 5 é treino intenso. Maior intensidade pode aumentar o risco de lesões.

- Tempo de Recuperação (dias): O número de dias necessários para a recuperação do jogador. Menor tempo de recuperação pode indicar sobrecarga e maior risco de lesões.

- Lesão: Variável alvo (binária), que indica se o jogador sofreu uma lesão (1) ou não (0).
Modelo/Algoritmo

O modelo utilizado é a Regressão Logística, um algoritmo de aprendizado supervisionado adequado para prever probabilidades em problemas binários (lesão ou não). O modelo é treinado com os dados históricos dos jogadores e avalia a probabilidade de lesão com base nos fatores mencionados.

# Objetivos
Prever a probabilidade de lesão: Estimar a chance de um jogador sofrer uma lesão com base em dados relacionados à idade, histórico de lesões, intensidade do treino e tempo de recuperação.
Ajuste dos planos de treinamento: Usar as previsões do modelo para ajustar a carga de treino e os períodos de recuperação, minimizando o risco de lesões.
Suporte para decisões clínicas e esportivas: Fornecer dados que ajudem equipes médicas e treinadores a monitorar o estado físico dos atletas e tomar decisões informadas sobre treinamento e recuperação.

# Etapas de Modelagem
Coleta e Preparação dos Dados:

Carregar o arquivo CSV com os dados dos jogadores.
Renomear as colunas conforme as especificações do projeto.
Separar as variáveis de entrada (X) e a variável alvo (y).
Dividir os dados em conjuntos de treinamento e teste.
Pré-processamento:

Normalizar os dados numéricos para garantir que todas as variáveis estejam na mesma escala.
Converter variáveis categóricas, como lesões anteriores, para valores binários.
Treinamento do Modelo:

Treinar o modelo de Regressão Logística com os dados normalizados de treino.
Ajustar os parâmetros do modelo conforme necessário.
Avaliação do Modelo:

Testar o modelo usando o conjunto de teste e avaliar a precisão das previsões.
Gerar uma matriz de confusão e relatório de classificação para analisar a performance do modelo.
Visualizar a matriz de confusão para entender os erros de classificação.
Previsões de Probabilidade:

Usar o modelo treinado para prever a probabilidade de lesão para jogadores não vistos durante o treinamento.
Ajustar os planos de treinamento com base nas probabilidades geradas pelo modelo.
Essas etapas garantem que o modelo seja eficaz em prever o risco de lesões e fornecer informações úteis para gerenciar o desempenho físico dos atletas.
