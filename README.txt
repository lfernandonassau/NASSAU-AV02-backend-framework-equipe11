#Sistema de Controle Financeiro - Backend

Este projeto consiste em uma aplicação back-end para controle financeiro pessoal, desenvolvida com **Python e Django**, que permite o gerenciamento de contas, categorias, transações, metas e rendas, além de autenticação segura via JWT.

 Objetivo do Projeto

Desenvolver uma API REST que implemente:

 Autenticação de usuários (registro e login)
 Operações CRUD completas
 Persistência em banco relacional
 Organização em camadas (Models, Views e URLs)
 Relacionamentos entre entidades financeiras

---

## 🛠 Tecnologias Utilizadas

* Python 3
* Django
* Django REST Framework
* SimpleJWT
* SQLite (banco de dados)
* Thunder Client / Insomnia (para testes)



 Estrutura do Projeto


financeair

 app_financeair
  migrations
  models.py
  serializers.py
  views.py
  urls.py

 financeair
  settings.py
  urls.py
  manage.py
  README.md




 Entidades do Sistema

1 Conta
2 Categoria
3 TipoTransacao
4 Transacao
5 MetaFinanceira
6 DespesaFixa
7 FonteRenda
8 Usuário (User - Django)

 Relacionamentos

 Usuário → Conta (1:N)
 Usuário → Categoria (1:N)
 Usuário → MetaFinanceira (1:N)
 Usuário → DespesaFixa (1:N)
 Usuário → FonteRenda (1:N)
 Conta → Transacao (1:N)
 Categoria → Transacao (1:N)
 TipoTransacao → Transacao (1:N)



 Autenticação

O sistema utiliza JWT para autenticação.

 Registro:


POST /api/auth/register/


 Login (Token):


POST /api/auth/token/


 Atualizar Token:


POST /api/auth/token/refresh/




 Endpoints Principais

Cada entidade possui os seguintes métodos:

 Método  Rota               Ação      
  
 GET     /api/contas       Listar    
 POST    /api/contas       Criar     
 GET     /api/contas/{id}  Detalhar  
 PUT     /api/contas/{id}  Atualizar 
 DELETE  /api/contas/{id}  Deletar   

Isso se repete para:

 categorias
 tipos
 transacoes
 metas  
 despesas
 rendas

Total: mais de 35 endpoints REST.



 Como Executar o Projeto

 1. Criar ambiente virtual


python -m venv venv
source venv/bin/activate   # Linux
venv\Scripts\activate      # Windows


 2. Instalar dependências


pip install django djangorestframework djangorestframework-simplejwt


 3. Migrar banco de dados


python manage.py makemigrations
python manage.py migrate


### 4. Criar superusuário


python manage.py createsuperuser


### 5. Rodar servidor


python manage.py runserver


Acesse:

* Admin: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
* API: [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)



 Testes

Os testes podem ser realizados usando:

 Thunder Client (VS Code)
 Insomnia
 Postman

Inclua o token JWT no cabeçalho:


Authorization: Bearer SEU_TOKEN_AQUI




 Observações

* O projeto utiliza SQLite por padrão, mas pode ser adaptado para MySQL ou PostgreSQL.
* Possui estrutura adequada para expansão futura.



 Integrantes do Grupo

(William Ângelo Ribeiro Santos
José Gustavo Tenório Guimarães
Ivan Pedro Batista dos Santos)



 Conclusão

O sistema cumpre todos os requisitos do projeto proposto, incluindo CRUD completo, autenticação JWT, banco relacional, organização em camadas e documentação básica para execução e testes.



 Desenvolvido como projeto acadêmico de Back-end Frameworks.