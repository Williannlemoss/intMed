# Medicar

## Sumário
<!--ts-->
* [Descrição do sistema](#Descrição)
* [Configuração](#Configuração)
    * [Backend](#Backend)
    * [Frontend](#Frontend)
* [URL](#URL)
    * [Backend](#URLBackend)
    * [Frontend](#URLFrontend)


<!--te-->

## Descrição

### Medicar é uma aplicação para auxiliar as clínicas com o gerenciamento de suas atividades no desenvolvimento do projeto, foi utilizado no back django e no front angular

## Configuração

### Vai ser apresentado as configurações necessárias para a utilização do sistema

## Backend

### 1- Fazer o clone do projeto no https://github.com/Williannlemoss/intMed.git

### 2- Criar um ambiente virtual venv dentro da pasta backend

### 3- Dentro da pasta backend tem um arquivo requirements.txt com todas as bibliotecas necessárias para o projeto e para instalá-las basta utilizar o comando ```pip install -r requirements.txt```

### 4- Dentro da pasta backend/setup tem um arquivo settings.py, dentro desse arquivo vai ter um atributo database, dentro dele altere o USER e o PASSWORD para o que você utiliza no postgres

### 5- Utilizar os comandos ```python manage.py makemigrations``` e depois ```python manage.py migrate``` para atualização do schema do banco de dados

### 6- Por último ```python manage.py runserver```

## Frontend

### 1- Com o projeto já clonado na configuração do [Backend](#Backend) basta entrar na pasta do frontend e executar o comando ```npm install``` ou ```yarn install``` para instalar as dependências do projeto.

### 2- Para execução do projeto basta utilizar o comando ```npm start``` ou ```ng server --o```

## URL

### Vai ser apresentado todas as urls do sistema tanto o [Backend](#URLBackend) quanto o [Frontend](#URLFrontend)


## URLBackend

### 1- Especialidade 

#### 1.1 GET /especialidades/

#### 1.2 GET /especialidades/&search=valor

#### 1.3 GET /especialidades/1/

#### 1.4 DELETE /especialidades/1/

#### 1.5 POST /especialidades/

#### exxplo de body para o POST: ```{'nome': 'especialidade'}```

### 2- Medico 

#### 2.1 GET /medicos/

#### 2.2 GET /medicos/?search=valor/?especialidade=valor

#### 2.3 GET /medicos/1

#### 2.4 DELETE /medicos/1/

#### 2.5 POST /medicos

#### exxplo de body para o POST: ``` { "nome": "Willian", "email": "will@gmail.com", "crm": "12312312-3", "telefone": "8888888888", "especialidade": 1 }```

### 3- Agenda 

#### 3.1 GET /agendas/

#### 3.2 GET /agendas/?medico=1&data_inicio=2021-05-25&data_final=2021-05-29

#### 3.3 GET /agendas/1

#### 3.4 DELETE /agendas/1/

#### 3.5 POST /agendas

#### exxplo de body para o POST: ``` { "dia": "2021-05-31", "medico": 1, "horario": ["09:00"] }```

### 4- Medico 

#### 4.1 GET /consultas/

#### 4.2 GET /consultas/1

#### 4.3 DELETE /consultas/1/

#### 4.4 POST /consultas

#### exxplo de body para o POST: ``` { "dia": "2021-06-10", "medico": 1, "horario": "11:00"}```

## URLFrontend

### 1- /login página inicial

### 2- /registro

### 3- /consulta
