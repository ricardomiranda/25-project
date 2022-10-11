# Módulo de Construção e Treinamento do Modelo

# Imports
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

print("\nPreparação do Modelo de Machine Learning.")

# Carrega os dados
print("\nCarregando o Conjunto de Dados...")
dados = pd.read_csv("../dados/dataset.csv")

# Variável alvo
target = "tendencia_mercado"

# Separa dados de treino e teste
x = dados.drop(columns = target)
y = dados[target]

# Divisão dos dados em treino e teste
print("\nDividindo os Dados em Treino e Teste...")
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.2)

# Cria o modelo
modelo = LinearRegression()

# Treina o modelo
print("\nTreinando o Modelo...")
modelo.fit(x_treino, y_treino)

# Faz as previsões com dados de teste
preds = modelo.predict(x_teste)

# Calcula o erro do modelo
erro_modelo = mean_absolute_error(y_teste, preds)

# Salva o modelo em disco
with open("../modelos/modelo_v1.pickle", "wb") as f:
    pickle.dump(modelo, f)

print("\nCarregando o Modelo Treinado...")

# Carrega o melhor modelo treinado
pickle_in = open("../modelos/modelo_v1.pickle", "rb")
modelo = pickle.load(pickle_in)

# Imprime as métricas e coeficientes
print("\nErro do Modelo Modelo (MAE): \n", erro_modelo)
print()
print("Coeficientes: \n", modelo.coef_)
print()
print("Intercepto: \n", modelo.intercept_)

# Faz previsões
print("\nPrevisão com Novos Dados...")
previsoes = modelo.predict(pd.DataFrame([[1,0,3,1]], columns = ["indice_bolsa_sp", "inflacao_alta", "taxa_desemprego", "taxa_juros"]))
print(previsoes)

print("\nModelo Criado com Sucesso.")



