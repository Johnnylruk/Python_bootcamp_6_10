from ETL_Pandas import pipeline_calc_kpi_sales
from user_call import requesting_file


folder, formatted_outcome = requesting_file()
pipeline_calc_kpi_sales(folder, formatted_outcome)
