# Projeto_IA_na_Educacao

## Motivação de projeto ##
Infelizmente, há vários problemas relacionado à acessibilidade da educação por parte do público estudantil, especialmente se observar no Brasil. Com esse tópico, teve-se a iniciativa de cria uma inteligência artificial a qual indicará cursos onlines para os usuários de acordo com suas necessidades e disponibilidades. O obejtivo é tornar a busca e aquisição mais fácil e acessível de cursos e aulas para os usuários.
A ideia surgiu inicalmente por meio de uma aula que teve como tema brainstorms para inteligências artificiais, então foi escolhida a ideia do aluno Gabriel Soares. 
Para a criação da IA, é necessário haver bastante pesquisa focada na área de Deep Learning, obter e analisar grandes bases de dados de cursos e de alunos, contendo suas disponiblidade financeiras e corriqueiras. Com as bases de dados, deve-se entender qual a necessidade dos usuários e saber aplicar bem as técnicas para relacioná-las com os problemas e a forma de solução.
Em geral, no mercado ja há alguns algoritmos que fazem tal objetivo, no entanto, por serem apenas algoritmos de divulgação e geralmente feito por grandes empresas, não são 100% eficiêntes e focados em resolver o problema abordado.
Com essa IA em bom funcionamento, deverá haver grandes chances de potencializar e aumento da educação e formação para o público estudantil.

## Funcionamento do projeto ##

Template:

Haverá um site ou dashboard o qual inicialmente o usuário se registrará, através de uma espécie de formulário, alguns dados pessoais, como nome, idade, estado civil e email. Em seguida, irá preencher  suas necessidades/interesses, o que inclui áreas de atuação e objetivos como entrar em certas empresas ou projetos pessoais acadêmicos. Também haverá um outro campo para preencher as disponibilidades do usuário, o que vai ter incluso para resposta suas condições financeiras e o seu tempo disponível para se dedicar aos cursos corriqueiramente. Tudo isso será especificado para o usuário, dizendo os motivos dos dados e o como eles serão usados para a busca dos cursos.
Após o registro, vai ser mostrado um menu, o qual terá uma aba para editar e vizualizar os campos preenchidos, funciona para caso se queira editar as informações, uma aba de transparência, especificando como a IA, e outra com todos os cursos encontrados . Destacademente, no painel principal, haverá logo alguns cursos populares que já batem com o que o usuário preencheu nos campos. Ao longo do tempo, conforme a IA for encontrado mais cursos, eles irão aparecer como disponível para começar.

INPUTS/OUTPUTS:

Como entrada, a IA terá os campos já citados preenchidos pelo usuário. Como saída, haverá um dashboard no menu do site, mostando os cursos encontrados que são de acordo com o que o usuário preencheu para os inputs. Ao encontrar os curos, será notificado no email do usuário, dizendo quais foram encontrados e suas informações como preço, área e horas para conclusão. Também serão mostrados cursos que a IA avaliou, porém não concluiu ideal para o usuário.

Camadas/Funcionamento:

A IA, com as informações dos inputs, buscará na internet sites de cursos, usando parâmetros como títulos, descrições, horas e preços. Cada curso irá passar por um processo de avaliação, sendo inicialmente armazenado como potencial de interesse, após isso calcula-se com funções probabilísticas se o curso é útil e viável para o usuário. Caso seja, irá para as etapas do output, os que não passarem pelas funções probabilísticas, irão ser jogados na aba que apresenta todos os cursos, para caso o usuário tenha interesse em analisá-los.

## Protótipo ##
O projeto consiste em:
  um código em c++ que pega o perfil de usuário e salva em um txt
  um código em R que filtra os cursos não-interessantes para o usuário e salva eles em um csv 
  2 códigos em python, que respectivamente treinam e aplicam o modelo de deep learning, e salva a saida em um arquivo txt
  outro código em R, que lê a saida em txt do modelo de DL, e com base nele cria um arquivo excel contendo cursos de interesse para o usuário
  e por fim, uma main em python que gerencia e compila tudo isso
  
Para o código funcionar corretamente é necessário:
  Ter instalado C++ e o compilador g++
  R
  Python
  as bibliotecas de python: pandas, scikitlearn, rpy2, pickle e subprocess (algumas talvez sejam padrão)
  
## Modo de uso ##
Para usar o programa, mova o diretório até a pasta src, e de lá, execute com o comando
python3 main.py (linux)
python main.py (windows)

## Alunos ##
Gabriel Soares - 20220077628

Pedro Miguel - 20220043110
