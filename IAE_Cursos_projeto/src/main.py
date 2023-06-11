import subprocess



def executarCpp():
    # Caminho para o arquivo C++
    caminho_arquivo_cpp = 'preferencias.cpp'

    # Compilar o arquivo C++
    subprocess.run(['g++', caminho_arquivo_cpp, '-o', '../bin/preferencias'])

    # Executar o arquivo C++
    processo = subprocess.Popen('../bin/preferencias')

    # Aguardar o término do process
    processo.communicate()
    

def executarR():
    # Caminho para o arquivo R
    caminho_arquivo_r = 'Filtro.R'

    # Executar o código R
    processo = subprocess.Popen(['Rscript', caminho_arquivo_r])

    # Aguardar o término do processo
    processo.wait()

#Chama as funções que executam os outros códigos
executarCpp()
print("#### Código em C++ compilado e executado ######")
executarR()
print("#### Código em R executado ######")

print("Pronto para Rodar o código em python...")

# * A base de dados vai ser salva com o nome udemy_courses_filtred.csv
# TODO: A partir daqui começa a main

