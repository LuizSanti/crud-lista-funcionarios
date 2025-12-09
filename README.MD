# 🏢 Sistema Web de Gerenciamento de Funcionários

## 📋 Descrição do Projeto

Este é um sistema web simples, desenvolvido utilizando o framework **Flask** (Python), que oferece uma interface completa para a gestão de dados de funcionários em uma empresa. O objetivo principal é demonstrar as operações básicas de banco de dados (CRUD) através de uma aplicação web.

---

### ✨ Funcionalidades Principais (CRUD)

O sistema permite realizar todas as operações essenciais no ciclo de vida do registro de um funcionário:

* **Criar (C) - Rota `/cadastrar`**: Adicionar novos funcionários ao banco de dados através de um formulário web.
* **Ler (R) - Rota `/listar`**: Visualizar todos os funcionários cadastrados em uma tabela organizada.
* **Consultar (R) - Rota `/consultar/<id>`**: Visualizar detalhes de um funcionário específico.
* **Atualizar (U) - Rota `/editar/<id>`**: Modificar os dados de um funcionário existente.
* **Deletar (D) - Rota `/deletar/<id>`**: Remover um registro de funcionário do banco de dados.

---

### 🚀 Requisitos para Rodar o Sistema

Para executar este projeto localmente, você precisa ter instalado:

1.  **Python 3.x**
2.  **MySQL Server** (Configurado com as credenciais `user='root'`, `password='root'` e o banco de dados `cadastro_funcionarios`).

#### Instalação das Dependências Python

Após clonar o repositório, navegue até a pasta do projeto e instale as bibliotecas necessárias:

```bash
pip install Flask mysql-connector-python

Como Iniciar o Servidor
1. Certifique-se de que o servidor MySQL está rodando.
2. Execute o arquivo principal da aplicação:
python app.py

Acesse a aplicação no seu navegador através do endereço: http://127.0.0.1:5000/

💾 Estrutura do Banco de Dados
O sistema utiliza um banco de dados MySQL chamado cadastro_funcionarios e se conecta à tabela funcionarios.

Tabela,Coluna,Tipo de Dado,Descrição
funcionarios,id,"INT (PK, Auto Increment)",Identificador único do funcionário.
,nome,VARCHAR(100),Nome completo.
,cargo,VARCHAR(50),Cargo atual na empresa.
,salario,"DECIMAL(10, 2)",Salário mensal.
,setor,VARCHAR(50),Departamento.
,telefone,VARCHAR(15),Telefone de contato.
,email,VARCHAR(100),E-mail corporativo.
,data_admissao,DATE,Data de entrada na empresa (Formato YYYY-MM-DD).

💻 Tecnologias Utilizadas

Categoria,Tecnologia,Função
Backend,Python,Linguagem de programação principal.
Framework,Flask,Micro-framework web utilizado para roteamento e lógica de aplicação.
Banco de Dados,MySQL,Sistema gerenciador de banco de dados relacional (SGBD).
Template Engine,Jinja2,Usado pelo Flask para renderizar HTML dinâmico.
Frontend,"HTML5, CSS3",Estrutura e estilização da interface.

🧑‍💻 Membros da Equipe

Nome do Membro,Função no Projeto,GitHub / Contato
[Luiz Gabriel],Desenvolvedor Front-End,[https://github.com/LuizSanti]
[Vinícius Nascimento],[Desenvolvedor Back-End],[https://github.com/vininascimentodev]