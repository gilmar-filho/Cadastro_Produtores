
# Prefeitura - Sistema de Cadastro de Pessoas

Este é um sistema simples de web cadastro de pessoas desenvolvido com Django, ideal para uso em prefeituras ou instituições públicas. O projeto permite cadastrar, listar, editar, deletar e exportar dados de cidadãos, com foco em simplicidade, funcionalidade e usabilidade.

O projeto ainda precisa ser lapidado e melhorado, porém as funcionalidades básicas (cadastro, atualização, busca e listagem) estão funcionando como o esperado.

## Funcionalidades

- Cadastro de pessoas (nome, email, telefone, data de nascimento).
- Listagem em tabela com paginação.
- Edição e exclusão de registros.
- Validação de dados via formulários Django.
- Exportação de dados em PDF (em breve).
- Interface amigável com Bootstrap 5.

## Estrutura do Projeto

```
prefeitura/
├── cadastro/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── templates/
│   │   └── cadastro/
│   │       ├── base.html
│   │       ├── listar_pessoas.html
│   │       ├── cadastrar_pessoa.html
│   │       ├── editar_pessoa.html
│   │       └── deletar_pessoa.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── prefeitura/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── Procfile
└── requirements.txt

```

## Requisitos

- Python 3.8 ou superior
- Django 5.x
- Bootstrap 5 (via CDN)
- SQLite (padrão no Django)

## Como rodar o projeto

1. Clone o repositório:
```bash
git clone https://github.com/gilmar-filho/Cadastro_Produtores.git
cd Cadastro_Produtores
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
venv\Scripts\activate    # No Windows
source venv/bin/activate   # No Linux/Mac
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Rode o servidor:
```bash
python manage.py runserver
```

6. Acesse em `http://127.0.0.1:8000/`

## Usuário admin (opcional)

Para acessar o painel administrativo:
```bash
python manage.py createsuperuser
```

Depois, entre em `http://127.0.0.1:8000/admin`

## Contribuições futuras

- Exportação em PDF por período
- Autocomplete na busca de nomes
- Autenticação de usuários
- Filtros por data