import sys
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


# Abre o arquivo em modo de escrita, truncando-o para ficar vazio
with open('../content/saida_predict.txt', 'w') as file:
    file.truncate(0)

# Redireciona a saída padrão para o arquivo
sys.stdout = open('../content/saida_predict.txt', 'w')


#Resultado do modelo com os novos inputs
predict = loaded_model.predict(input_test)
for i in predict:
    print(int(i))


# Fecha o arquivo
sys.stdout.close()

# Restaura a saída padrão para o console
sys.stdout = sys.__stdout__