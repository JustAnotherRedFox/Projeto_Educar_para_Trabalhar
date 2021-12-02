--------- MANUAL DE INSTRUCOES -------
no menu iniciar deve-se escolher oque o usuario deseja fazer, digitando:
'C' para cadastrar um novo cliente
'L' para listar todos os clientes cadastrados
'D' para deletar os dados de um cliente cadastrado
'B' para buscar os dados de um cliente cadastrado
'S' para sair do programa

 ---- C (cadastro) ----

 os campos destacadas devem ser preechidos:
 nome: de preferencia um com 4 ou mais letras
 email: de preferencia um com 8 ou mais letras seguindo o exemplo nome@dominio.com
 telefone: de preferencia seguindo o seguinte exemplo: (71)90000-0000
 endereco: de preferencia 8 ou mais letras
 data de nascimento: de preferencia com 8 letras seguindo o exemplo: (dd/mm/aaaa)a {dia/mes/ano}
 genero: o genero do cliente, unicamente F(feminino) ou M(masculino)
 Cpf: digite o CPF do cliente seguindo o exemplo: 000.000.000-00

 ---- L (listar) ----

 ira listar os clientes cadastrados, se nenhum cliente for cadastrado retornara erro
 ira apenas informar dados basicos para todos os dados use a funcao de busca
 listando os seguintes dados:
 ID: usado para buscar e deletar cadastro, este numero sera mudado se um ID anterior for deletado
 nome: nome do cadastro
 genero: genero do cadastro
 cpf: cpf do cadastro

 ---- D (deletar) ----

 ira deletar um cadastro
 para deletar um cadastro o usuario deve informar o ID do cadastro e confirmar a exclusao.
 confirmado a exclusao o cadastro sera permantemente deletado

 ---- B (buscar) ----

 usado para buscar dados de um cadastro
 pode-se usar para ler os dados completos do cliente, tais como:
 ID, nome, email, telefone, endereco, data de nascimento, genero e cpf.

 ---- S (sair) ----

 usado para encerrar o programa
 as alteracoes feitas dentro do programa nao seram salvos
 os dados seram perdidos pela falta de um banco de dados
 todos os dados deveram ser cadastrados novamente a cada execusao.
