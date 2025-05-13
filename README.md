Documentação referente ai Desafio Técnico – Desenvolvedor(a) Back-end Sênior

✨ Requisitos do Desafio realizados
🔹 Funcionalidades Implementadas

Autenticação e Gerenciamento de Usuários
- Cadastro e login de usuários (simples, com e-mail/senha).
- Uso de tokens JWT para autenticação.

Gestão de Documetos
- Endpoint para armazenar e listar documentos digitais (exemplo: identidade, CPF, comprovante de vacinação).

Gestão de Transporte Público
- Endpoint para consultar saldo do passe de transporte público (mockado).
- Endpoint para simular recarga do passe.

🔹 Requisitos Técnicos utilizados
FastAPI como framework principal.
Banco de Dados Relacional utilizando PostgreSQL e ORM como SQLAlchemy.
Ferramenta de migrations utilizando Alembic
Testes da rota de usuários utilizando pytest

🏗️ Como rodar o projeto
- Instalar ambiente virtual usando venv
- Instalar dependências: pip install -r requirements.txt
- Subir banco de dados: make psql-up
- Rodar os testes: pytest
