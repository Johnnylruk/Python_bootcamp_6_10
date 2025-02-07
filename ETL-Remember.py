import csv

file_name = "REMEMBEER PUB PARNAIBA - consumos.csv"

def read_file(file_name):
	data = []
	with open(file_name, mode='r', encoding='utf-8') as file:
		read_csv = csv.DictReader(file)
		for line in read_csv:
			data.append(line)
		return data

def process_file(file):
	
	filter_gender = []
	for data in file:
		filter_gender.append(data['nome'])
		if data['genero'] != '':
			filter_gender.append(data['genero'])
	filter_gender.sort()
	splitted_name = [name.split(' ') for name in filter_gender]
	return splitted_name

remember_file = read_file(file_name)

list_of_filtered_names = process_file(remember_file)

def putting_feminino(list):
	new_list = list.copy()
	for pos, first_name in enumerate(list):
		if first_name[0][-1] in 'Aa':
			if len(first_name) == 2:
				list_to_insert = [first_name, 'Feminino']
				new_list.insert(pos,list_to_insert)
	return new_list
	
list_of_filtered_names = putting_feminino(list_of_filtered_names)







  		
		