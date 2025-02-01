import csv


def read_file(file_name) -> list:
  with open(file_name, mode='r', encoding='utf-8') as file:
    read_csv = csv.DictReader(file)
    return list(read_csv)
  
def process_data(file: list) -> dict:

    processed_file: dict = {}

    for item in file:
        category = item['Categoria']
        if category not in processed_file:
            processed_file[category] = []
        processed_file[category].append(item)
    return processed_file

def calc_sales_per_category(data):
    sales_per_category: dict = {}
    for category, items in data.items():
        total_sales = sum(int(item['Quantidade']) * int(item['Venda']) for item in items)
        sales_per_category[category] = total_sales
    return sales_per_category

def main():
   
    file_name  = 'example.csv'
    raw_data = read_file(file_name)
    data_processed = process_data(raw_data)
    sales_per_category = calc_sales_per_category(data_processed)

    for category, total in sales_per_category.items():
       print(f'{category}, ${total}')


if __name__ == '__main__':
   main()
  

