import rpy2.robjects.packages as rpackages
from rpy2.robjects.vectors import StrVector
import subprocess

def is_package_installed(package_name):
    try:
        rpackages.importr(package_name)
        return True
    except ImportError:
        return False


def executarModeloDeepLearning():
    caminho_arquivo_train = 'train.py'
    caminho_arquivo_predict = 'predict.py'
    
    #Roda o arquivo de treino
    processo_treino = subprocess.Popen(['python',caminho_arquivo_train])
    
    #Espera ele terminar de ser executado
    processo_treino.wait()

    #Roda o modelo de DL
    processo_predict = subprocess.Popen(['python',caminho_arquivo_predict])

    #Espera o mesmo terminar de ser executado mas podendo interagir com as saidas
    processo_predict.communicate()


def executarCpp():
    # Caminho para o arquivo C++
    caminho_arquivo_cpp = 'preferencias.cpp'

    # Compilar o arquivo C++
    subprocess.run(['g++', caminho_arquivo_cpp, '-o', '../bin/preferencias'])

    # Executar o arquivo C++
    processo = subprocess.Popen('../bin/preferencias')

    # Aguardar o término do process
    processo.communicate()
    

def filtrar():
    # Caminho para o arquivo R
    caminho_arquivo_r = 'Filtro.R'

    # Executar o código R
    processo = subprocess.Popen(['Rscript', caminho_arquivo_r])

    # Aguardar o término do processo
    processo.wait()

def recomendar():
    #caminho para o arquivo R
    caminho_arquivo_r = 'recomendados.R'

    if not is_package_installed("openxlsx"):
        print("O pacote 'openxlsx' não está instalado. Instalando...")
        utils = rpackages.importr("utils")
        utils.install_packages(StrVector(["openxlsx"]))

    # Carregar o pacote "openxlsx"
    openxlsx = rpackages.importr("openxlsx")

     # Executar o código R
    processo = subprocess.Popen(['Rscript', caminho_arquivo_r])

    # Aguardar o término do processo
    processo.wait()

#Chama as funções que executam os outros códigos
executarCpp()
print("#### Código em C++ compilado e executado, perfil de usuario obtido ######")
filtrar()
print("#### Código em R executado, arquivo base filtrado ######")

print("Pronto para Rodar o código em python...")
executarModeloDeepLearning()
print("#### Modelo de Deep Learning Executado ######")
print("#### Executando código em R para fazer as recomendações")
recomendar()
print("#### Código em R executado, recomendações feitas ######")
print("#### Arquivo de excel Recomendações.xlsx gerado ######")


