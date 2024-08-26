# Ingestão de dados

Este documento serve como uma referência rápida e clara para a implementação e uso do pipeline de ingestão de dados, abordando as funções principais de cada componente e descrevendo os passos necessários para configurar e executar o sistema.


## Documentação dos Arquivos de Código

- api.py: este arquivo contém o código responsável por fazer a requisição à API e obter dados de Pokémon;

- função get_pokemon(): faz uma requisição GET à PokeAPI para obter uma lista de todos os Pokémon. Se a requisição for bem-sucedida, retorna os dados no formato JSON; caso contrário, retorna None;

- clickhouse_client.py: este arquivo gerencia a conexão com o banco de dados ClickHouse;

- função get_client(): conecta ao cliente ClickHouse usando as variáveis de ambiente configuradas;

- função execute_sql(script_path): executa um script SQL no banco de dados ClickHouse;

- função insert_dataframe(client, table_name, df): insere um DataFrame em uma tabela especificada do ClickHouse;

- data_processing.py: este arquivo lida com o processamento de dados antes de serem inseridos no ClickHouse;

- função process_data(data): cria um DataFrame e o salva em formato Parquet;

- função prepare_dataframe_for_insert(df): prepara um DataFrame para inserção no ClickHouse, incluindo uma coluna de timestamp e outra de tags;

- minio_client.py: este arquivo gerencia o armazenamento de arquivos no MinIO;

- função create_bucket_if_not_exists(bucket_name): cria um bucket no MinIO caso ele não exista;

- função upload_file(bucket_name, file_path): faz o upload de um arquivo para o MinIO;

- função download_file(bucket_name, file_name, local_file_path): faz o download de um arquivo do MinIO para um caminho local;

- create_table.sql: este arquivo SQL cria a tabela working_data no ClickHouse, que será usada para armazenar os dados ingeridos;

- comando CREATE TABLE IF NOT EXISTS working_data: define a estrutura da tabela, incluindo as colunas data_ingestao, dado_linha, e tag. A tabela usa o mecanismo MergeTree e é ordenada pela coluna data_ingestao.


## Funcionalidades

- **Ingestão de Dados**: Aquisição de dados através de uma API que retorna informações em formato JSON, prontos para processamento.

- **Armazenamento no MinIO**: Armazenamento de dados em formato Parquet dentro do ecossistema MinIO, garantindo acessibilidade e escalabilidade.

- **Integração com ClickHouse**: Processamento e inserção de dados na tabela `working_data` do ClickHouse para análises avançadas.

- **Testes Automatizados**: Implementação de testes usando pytest para validar cada componente, garantindo que o sistema opere corretamente sob várias condições.


## Pré-requisitos

- **Python 3.12+**
- **Poetry** 
- **Docker e Docker Compose**


## Configuração

1. **Clone o repositório:**

   ```bash
   git clone [text](https://github.com/BeatrizHirasaki/Ingestao-dados-M11)
   cd Ingestao-dados-M11
   ```

2. **Instale as dependências:**

    ```bash
    poetry install
    ```

3. **Configure as variáveis de ambiente:**

- Crie um arquivo .env na raiz do projeto.
- Defina as variáveis de ambiente para MinIO e ClickHouse.
- Suba os serviços no Docker:

    ```bash
    docker-compose up --build
    ```


## Execução da aplicação

- Inicie o servidor:

    ```bash
    poetry run python app.py
    ```

- Inicialize o docker com:

    ```bash
    docker-compose up --build
    ```

- Ao acessar ao localhost:9000 a interface do minIO será aberta.

- Rode o codigo com o comando:

    ```bash
    poetry run python app.py
    ```

- Para rodar os testes use:

    ```bash
    poetry run pytest
    ```