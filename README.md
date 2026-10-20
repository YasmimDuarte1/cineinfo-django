# Desafio CineInfo

Projeto Django da prática "O Desafio CineInfo": criação do model `Filme` (título, ano, sinopse), migrações, cadastro de 10 filmes pelo Django Admin e consulta ao banco `db.sqlite3`.

## Estrutura

- Projeto Django: `cineinfo/`
- App: `filmes/` — model `Filme` (`titulo`, `ano`, `sinopse`) registrado no Admin

## Como rodar

```bash
cd cineinfo_django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/admin/` para gerenciar os filmes.

## Banco de dados

O `db.sqlite3` já está populado com 10 filmes cadastrados pelo Admin, na tabela `filmes_filme`.
