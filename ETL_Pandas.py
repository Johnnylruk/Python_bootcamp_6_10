import pandas as pd
import os
import glob


def extract_json(folder: str) -> pd.DataFrame:

  '''This is for read and concat all json files inside a folder'''

  files_json = glob.glob(os.path.join(folder, '*.json')) # This is for list json files
  df_list = [pd.read_json(files) for files in files_json]
  df_concat = pd.concat(df_list, ignore_index=True)
  return df_concat

def transform_file(df: pd.DataFrame) -> pd.DataFrame:

  '''This is for add another column into the DF'''
  df = extract_json('data')

  df['Total_KPI'] = df['Quantidade'] * df['Venda']
  return df


def load_dataframe(df: pd.DataFrame, format_outcome: list):

    for format in format_outcome:
        if format == 'csv':
            df.to_csv('new_df.csv')
        if format == 'parquet':
            df.to_parquet('new_df.parquet')


def pipeline_calc_kpi_sales(folder: str, outcome_format):
    df = extract_json(folder)
    df_formatted = transform_file(df)
    load_dataframe(df_formatted, outcome_format)

   