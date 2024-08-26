import pytest
from unittest.mock import patch, Mock
import pandas as pd
from data_pipeline.data_processing import process_data, prepare_dataframe_for_insert

def test_process_data():
    # Dados de entrada
    data = {'column1': [1, 2], 'column2': [3, 4]}
    # Mock datetime e pyarrow
    with patch('data_pipeline.data_processing.datetime') as mock_datetime, \
         patch('data_pipeline.data_processing.pq.write_table') as mock_write_table:
        mock_datetime.now.return_value.strftime.return_value = '20240101010101'
        filename = process_data(data)
        
        assert filename == 'raw_data_20240101010101.parquet'
        # Verifica se o write_table foi chamado
        assert mock_write_table.called
        # Verifica se o Table.from_pandas foi chamado corretamente dentro de process_data
        mock_write_table.assert_called_once()

def test_prepare_dataframe_for_insert():
    # Criando um DataFrame de exemplo
    df = pd.DataFrame({
        'column1': [1, 2],
        'column2': ['text1', 'text2']
    })
    # Mock datetime
    with patch('data_pipeline.data_processing.datetime') as mock_datetime:
        mock_datetime.now.return_value = pd.Timestamp('2024-01-01 00:00:00')
        df['data_ingestao'] = pd.Timestamp('2024-01-01 00:00:00')
        df['tag'] = 'example_tag'
        expected_json = df.apply(lambda row: row.to_json(), axis=1)
        expected_json.name = 'dado_linha'  # Atribuir o mesmo nome da série no DataFrame resultante

        result = prepare_dataframe_for_insert(df)

        # Verifique se as colunas corretas estão presentes
        assert list(result.columns) == ['data_ingestao', 'dado_linha', 'tag']
        # Verifique se a coluna 'data_ingestao' está correta
        assert (result['data_ingestao'] == pd.Timestamp('2024-01-01 00:00:00')).all()
        # Verifique se a coluna 'tag' está correta
        assert (result['tag'] == 'example_tag').all()
        # Verifique se a conversão para JSON está correta
        pd.testing.assert_series_equal(result['dado_linha'], expected_json, check_names=True)  # Certifique-se de que os nomes também são comparados
