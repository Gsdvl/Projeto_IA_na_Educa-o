#include <iostream>
#include <fstream>


using namespace std;


bool salvarPreferencias(float orcamento, int duracaoCurso, int nivelCurso, int areaEstudo)
{
    // !Condições de erro
    if(orcamento < 0 || orcamento > 200) return false;
    if(duracaoCurso < 0 || duracaoCurso > 3) return false;
    if(nivelCurso < 0 || nivelCurso > 4) return false;
    if(areaEstudo < 0 || areaEstudo > 4) return false;


    fstream arquivo;
    arquivo.open("../content/preferencias.txt", ios::out | ios::trunc);
    arquivo << orcamento << endl;
    arquivo << duracaoCurso << endl;
    arquivo << nivelCurso << endl;
    arquivo << areaEstudo << endl;

    //A função foi executada corretamente
    return true;
}

int main()
{
    float orcamento;
    int duracaoCurso;
    int nivelCurso;
    int areaEstudo;

    while(true){
        cout << "Qual o orcamento: (entre 0 e 200)" << endl;
        cin >> orcamento;
        cout << "Cursos curtos, medios ou longos? (1,2,3)" << endl;
        cin >> duracaoCurso;    
        cout << "Deseja um curso de nível iniciante, intermediário, avançado ou para todos os níveis? (1,2,3,4)" << endl;
        cin >> nivelCurso; 
        cout << "Qual é a sua área de interesse?" << endl;
        cout << "(1) Business Finance   |  (2) Graphic Design | (3) Musical Instruments    |   (4) Web Development" << endl;
        cin >> areaEstudo;
        
        if (salvarPreferencias(orcamento, duracaoCurso, nivelCurso, areaEstudo)) break;
        else cout << "Alguma entrada foi inválida, refaça o seu perfil" << endl;
    }
    return 0;
}