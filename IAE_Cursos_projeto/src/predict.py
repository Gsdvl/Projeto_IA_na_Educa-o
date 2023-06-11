from train import *

#Carrega o modelo
with open('../bin/model.pkl', 'rb') as mdl:
    loaded_model = pickle.load(mdl)

#Carrega o arquivo de entrada
with open('../content/preferencias.txt', 'r') as file:
    preferencias = file.read()

#Cria o array de input e o preenche
input_test = [[], [], [], []]
for i, v in enumerate(preferencias.split()):
    input_test[i].append(int(v))
    
#Resultado do modelo com os novos inputs
predict = loaded_model.predict(input_test)
for i in predict:
    print(int(i))