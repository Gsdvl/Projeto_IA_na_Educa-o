#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int contarLinhas(string caminhoArquivo)
{
    int linhas = 0;
    string linha;
    fstream arquivo;
    arquivo.open(caminhoArquivo, ios::in);

    while(getline(arquivo, linha))
    {
        linhas++;
    }
    return linhas;

}


int main()
{
    string caminhoArquivo = "../content/recomendacoes.txt";
    string linha;
    int linhas = contarLinhas(caminhoArquivo);
    int opt;
    vector <string> rejeitados;
    vector <string> temp;

    fstream arquivo;
    arquivo.open(caminhoArquivo, ios::in);

    while (getline(arquivo, linha)) {
      temp.push_back(linha);
    }
    arquivo.close();

    for(int i = 0; i < linhas/2; i++)
    {
        cout << temp[i] << "-" << temp[(linhas/2)+i] << endl;
        cout << "Você gostou do curso recomendado?" << endl;
        cout << "0 - Não" << endl;
        cout << "1 - Sim" << endl;
        cout << "2 - Não quero continuar avaliando" << endl;
        cin >> opt;
        switch(opt)
        {
            case 0:
                rejeitados.push_back(temp[linhas/2+i]);
            break;
            case 1:
            break;
            case 2:
                opt = -1;
            break;
        }
        if(opt == -1) break;
    }

    
    fstream arquivoRejeitados;
    arquivoRejeitados.open("../content/rejeitados.txt", ios::out | ios::trunc);
    
    for(int i = 0; i < rejeitados.size(); i++)
    {
        arquivoRejeitados << rejeitados[i] << endl;
    }
    arquivoRejeitados.close();
    return true;





    return 0;
}
