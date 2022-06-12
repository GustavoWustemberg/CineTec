#1.	Tema
O tema Cinema foi escolhido pelo professor Emerson trazendo a ideia de criação de funções usando a bilheteria (visualização de filmes, busca, compra) e lanchonete (visualização de produtos para comprar, alteração de preço)

##1.2 Objetivos
Com base nos levantamentos realizados, chegamos aos seguintes objetivos:

###1.2.1 Objetivo Geral
Construir um software para gerenciamento de filmes do cinema e produtos em catálogo na lanchonete a partir de funções.

###1.2.2 Objetivos Específicos

<li>isualização de filmes em cartaz, através de solicitação do cliente.</li>
<li>Busca por algum filme em específico.</li>
<li>Compra de filme que estiver de seu agrado.</li>
<li>Lista os produtos em estoque que o cliente deseja ver na lanchonete.</li>
<li>Busca um produto específico que consta no catálogo.</li>
<li>Adiciona produtos e alterar seus preços.</li>
 
#2.	TECNOLOGIAS
 
##2.1 Python
 
Figura 1 – Logo Python 

#3.	DESENVOLVIMENTO DO PROJETO

De início é criado um if e elif para apresentar os menus de navegação, sendo eles: Bilheteria e Lanchonete.
A partir da escolha do cliente, será apresentado 8 funções para todo sistema, sendo elas 3 para bilheteria e 5 para a lanchonete.

Def ListarFilmes():
Para listar filmes, colocamos dentro da função “ListarFilmes()” os filmes em uma variável de tipo lista. Quando inserida, é feito uma chamada a partir de vetores dentro da variável “filmes” e coloca tudo dentro de um print usando um .format.
Serve para listar’ todos os filmes disponíveis na bilheteria.

Def BuscarFilme():
A busca de algum filme é feita a partir da função “BuscarFilme()”. Permite que seja inserido o nome do filme desejado em um input e te informa, caso ele não esteja em cartaz, através de um print usando if ou else.
Usado para buscar um filme específico estando em cartaz ou não.

Def Comprar():
A compra de um ingresso desejado foi feita a partir da função “Comprar()”. Os filmes em cartaz são apresentados através de um print seguido de 4 perguntas para confirmação de informações. Dentro de cada input apresentado é mencionado o filme desejado, quantidade de ingressos, se é estudante e quantos são estudantes. Usando if, elif e else para direcionar as respostas por meio de variáveis Int.
Usado para compra de ingressos de filmes disponíveis.

Def listar():
Na função “listar()” é colocado um print da variável de tipo dicionário chamada “lista”.
Lista todos os produtos da lanchonete disponíveis no catálogo.

Def buscar():
Na função “buscar()” é adicionada um input para que o cliente digite o produto, caso não esteja em catálogo, o sistema enviará um print dizendo: "Este produto não consta no catalogo".
Busca um produto específico da lanchonete.

Def adicionar():
São colocados dois inputs na função “adicionar()” para que seja adicionado o nome e preço do produto na lista. Ao ser adicionado, ele retorna uma mensagem através do print dizendo “Cadastro realizado com sucesso! ”.
Adiciona algum produto ao catálogo.

Def alterar():
Dentro da função “alterar()” é colocado um input questionando qual o produto a ter o seu valor alterado, logo em seguida um input para você digitar a alteração. Caso o produto não esteja no catálogo, é retornado dentro de um print a mensagem: "Este produto não consta no catalogo".
Altera valor no catálogo da lanchonete.

Def listarNomes():
Com a função “listarNomes()”, é apresentado um print dos produtos em um for que lista somente os nomes.
Listar os produtos disponíveis sem os preços.
