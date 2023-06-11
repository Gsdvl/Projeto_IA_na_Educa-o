import random
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

#Arquivo filtrado pelo R
arquivo = pd.read_csv('../content/udemy_courses_filtred.csv')

dados = [[], [], [], []] #Array input
subscribers = list() #Array output

#Pondo os dados no array input:
with open('../content/preferencias.txt', 'r') as file:
    preferencias = file.read()

for i, v in enumerate(preferencias.split()):
    dados[i].append(int(v))

#Como os arrays tem que ter o mesmo tamanho, seleciona-se 4 números aleatorios do csv entre zero e o tamanho da coluna, e armazena no array output:
size = len(arquivo["num_subscribers"])
menor = min(arquivo["num_subscribers"])
maior = max(arquivo["num_subscribers"])

for s in range(4):
    n = random.randint(0, size-1)
    subscribers.append(arquivo["num_subscribers"][n])

#Treina o modelo
while True:
    dados_train, dados_test, subscribers_train, subscribers_test = train_test_split(dados, subscribers, train_size=0.5, random_state=42)

    model = LinearRegression()
    model.fit(dados_train, subscribers_train)
    mdl = model.predict(dados)
    if menor <= min(mdl) or maior >= max(mdl):
        break

#Cria um arquivo do modelo
with open('../bin/model.pkl', 'wb') as file:  
    pickle.dump(model, file)