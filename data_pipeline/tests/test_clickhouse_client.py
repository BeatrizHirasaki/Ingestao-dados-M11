import pytest
from unittest.mock import patch, MagicMock
from data_pipeline.clickhouse_client import execute_sql_script, get_client, insert_dataframe
import clickhouse_connect
import os
from dotenv import load_dotenv
from unittest import mock

# Teste para get_client
@mock.patch('clickhouse_connect.get_client')
def test_get_client(mock_get_client):
    mock_get_client.return_value = mock.Mock()
    client = get_client()
    
    mock_get_client.assert_called_once_with(
        host=os.getenv('CLICKHOUSE_HOST'),
        port=os.getenv('CLICKHOUSE_PORT'),
    )
    assert client is not None

def test_execute_sql_script():
    mock_client = MagicMock()
    with patch('data_pipeline.clickhouse_client.get_client', return_value=mock_client), \
         patch('builtins.open', mock.mock_open(read_data='SELECT * FROM table;')), \
         patch('data_pipeline.clickhouse_client.get_client.execute') as mock_execute:
        execute_sql_script('path/to/sql_script.sql')
        mock_client.command.assert_called_once_with('SELECT * FROM table;')

def test_insert_dataframe():
    mock_client = MagicMock()
    df = MagicMock()  # Você pode substituir por um DataFrame real para testes mais integrados.
    table_name = "test_table"

    insert_dataframe(mock_client, table_name, df)

    mock_client.insert_df.assert_called_once_with(table_name, df)