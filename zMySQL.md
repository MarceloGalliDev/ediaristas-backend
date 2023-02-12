# Comandos MySQL
## Conexão MySQL
> Conectando no banco
    - mysql -h NOME-DO-SERVIDOR -u NOME-DO-USUARIO
        - caso seja um servidor local, usar localhost no NOME-DO-SERVIDOR
> Conectando no banco como root
    - mysql -u root -p
      - digite o password do mysql
    - se acaso nao funcionar
        - sudo nano /etc/paths (comando no terminal)
        - adicione na ultima linha
            - /usr/local/mysql/bin
        - fexe o terminal e reabra

## Comandos
> CREATE DATABASE nome-do-banco;
    - criando database
> SHOW DATABASES | TABLES;
    - exibindo os bancos criados ou tabelas criadas
> USE nome-da-database | nome-da-table;
    - usando a database antes de criar table
> DESC nome-da-table;
    - para verificar informações sobre uma table
> DROP DATABSE nome-do-banco | TABLE nome-da-table;
    - para deletar database e tabelas
> TRUNCATE TABLE nome-da-table;
    - esse comando limpa os dados da tabela e recria com o mesmo formato