import pandas as pd
import os
import glob
from utils_logs import log_decorator, time_measure_decorator

@log_decorator
def extract_json(folder: str) -> pd.DataFrame:

  '''This is for read and concat all json files inside a folder'''

  files_json = glob.glob(os.path.join(folder, '*.json')) # This is for list json files
  df_list = [pd.read_json(files) for files in files_json]
  df_concat = pd.concat(df_list, ignore_index=True)
  return df_concat

@log_decorator
@time_measure_decorator
def transform_file(df: pd.DataFrame) -> pd.DataFrame:

  '''This is for add another column into the DF'''
  df = extract_json('data')

  df['Total_KPI'] = df['Quantidade'] * df['Venda']
  return df

@log_decorator
def columns_from_portuguese_to_english(df: pd.DataFrame) -> pd.DataFrame:
    df_to_rename = df
    df_to_rename = df_to_rename.rename(columns={'Produto': 'Product', 'Categoria': 'Category', 'Quantidade': 'Quantity', 'Venda': 'Sales','Data': 'Date'})
    return df_to_rename

@log_decorator
def load_dataframe(df: pd.DataFrame, format_outcome: list):

    for format in format_outcome:
        if format == 'csv':
            df.to_csv('new_df.csv')
        if format == 'parquet':
            df.to_parquet('new_df.parquet')

@log_decorator
def pipeline_calc_kpi_sales(folder: str, outcome_format):
    df = extract_json(folder)
    df_formatted = transform_file(df)
    df_english = columns_from_portuguese_to_english(df_formatted)
    load_dataframe(df_english, outcome_format)