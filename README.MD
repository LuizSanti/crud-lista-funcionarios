# 🏢 Sistema Web de Gerenciamento de Funcionários

## 📋 Descrição do Projeto

Este é um sistema web simples, desenvolvido com **Flask (Python)**, que oferece uma interface completa para a gestão de dados de funcionários. O objetivo principal é demonstrar as operações **CRUD** (Create, Read, Update, Delete) através de uma aplicação web conectada ao MySQL.

---

### ✨ Funcionalidades Principais (CRUD)

O sistema permite gerenciar o ciclo de vida dos registros:

* **Criar (C) - `/cadastrar`**: Adicionar novos funcionários.
* **Ler (R) - `/listar`**: Visualizar todos os funcionários em tabela.
* **Consultar (R) - `/consultar/<id>`**: Ver detalhes de um funcionário específico.
* **Atualizar (U) - `/editar/<id>`**: Modificar dados existentes.
* **Deletar (D) - `/deletar/<id>`**: Remover um registro.

---

### 🚀 Requisitos para Rodar o Sistema

Para executar este projeto localmente, você precisa ter instalado:

1.  **Python 3.x**
2.  **MySQL Server** (Configurado com credenciais `user='root'`, `password='root'` e o banco de dados `cadastro_funcionarios`).

#### Instalação das Dependências Python

Navegue até a pasta do projeto e instale as bibliotecas necessárias:

```bash
pip install Flask mysql-connector-python

### Como Iniciar o Servidor

1. Certifique-se de que o servidor MySQL está rodando.
2. Execute o arquivo principal da aplicação:

```bash
python app.py

3. Acesse a aplicação no seu navegador: http://127.0.0.1:5000/

### 💾 Estrutura do Banco de Dados

O sistema utiliza o banco cadastro_funcionarios e a tabela funcionarios, que possui a seguinte estrutura:

Coluna         Tipo de Dado                 Descrição
---------------------------------------------------------------
id             INT (PK, Auto Increment)     Identificador único do funcionário.
nome           VARCHAR(100)                 Nome completo do funcionário.
cargo          VARCHAR(50)                  Cargo ocupado na empresa.
salario        DECIMAL(10,2)                Salário mensal do funcionário.
data_admissao  DATE                          Data de admissão (formato YYYY-MM-DD).


### 💻 Tecnologias Utilizadas

Categoria        Tecnologia        Função
---------------------------------------------------------------
Backend          Python            Linguagem principal.
Framework        Flask             Roteamento e lógica da aplicação.
Banco de Dados   MySQL             SGBD relacional.
Template Engine  Jinja2            Renderização de HTML dinâmico.
Frontend         HTML5, CSS3       Estrutura e estilização.

### 🧑‍💻 Membros da Equipe

Nome do Membro          Função no Projeto	            GitHub    
---------------------------------------------------------------
Luiz Gabriel	          Desenvolvedor Front-End       https://github.com/LuizSanti
Vinicius Nascimento	    Desenvolvedor Back-End	      https://github.com/vininascimentodev
