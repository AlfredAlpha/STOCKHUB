# StockHub

StockHub é uma aplicação web desenvolvida para a Optfiber Telecomunicações LTDA, com o objetivo de centralizar o registro e gerenciamento de modems e roteadores instalados nas residências dos clientes. A solução visa melhorar a gestão de equipamentos e o atendimento ao cliente, oferecendo uma interface simples e eficiente.

## Funcionalidades
- **Registro de Equipamentos**: Adicione novos modems/roteadores com modelo, número de série, nome do cliente e data de instalação.
- **Listagem**: Visualize todos os equipamentos registrados.
- **Busca**: Pesquise equipamentos por número de série ou nome do cliente.

## Tecnologias Utilizadas
- **Backend**: Python (Flask)
- **Banco de Dados**: MySQL
- **Frontend**: HTML, CSS
- **Controle de Versão**: Git/GitHub

## Pré-requisitos
- Python 3.x
- MySQL Server
- Git

## Instalação
1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/AlfredAlpha/STOCKHUB.git
   cd STOCKHUB

2. **Instale as Dependências:**
    ````bash
    pip install flask mysql-connector-python

3. **Configure o Banco de Dados**:
* Crie o banco de dados no MySQL:
    ````sql
    CREATE DATABASE stockhub_db;
    USE stockhub_db;
    CREATE TABLE equipamentos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        modelo VARCHAR(100) NOT NULL,
        numero_serie VARCHAR(50) UNIQUE NOT NULL,
        cliente_nome VARCHAR(100) NOT NULL,
        data_instalacao DATE NOT NULL
    );

* Atualize as credenciais no arquivo app.py:
    ````python
    db_config = {
        'host': 'localhost',
        'user': 'seu_usuario',
        'password': 'sua_senha',
        'database': 'stockhub_db'
    }

4. **Execute a Aplicação:**
    ````bash
    python app.py
    * Acesse em http://127.0.0.1:5000/ no navegador.

**Design**

Cores: Grafite (#333333) como fundo principal e amarelo (#FFC107) como destaque, refletindo a identidade da Optfiber Telecomunicações LTDA.
Subtons: Cinza claro (#f5f5f5) e variações para contraste e harmonia.

**Próximos Passos**
Adicionar edição e exclusão de registros.
Implementar autenticação de usuários.
Criar relatórios de manutenção e inventário.

**Contribuição**
1. Faça um fork do repositório.
2. Crie uma branch para sua feature (git checkout -b feature/nova-funcionalidade).
3. Commit suas mudanças (git commit -m "Adiciona nova funcionalidade").
4. Envie para o GitHub (git push origin feature/nova-funcionalidade).
5. Abra um Pull Request.

**Licença**
Este projeto é de uso interno da Optfiber Telecomunicações LTDA e não possui licença pública no momento.

Desenvolvido por AlfredAlpha e equipe.