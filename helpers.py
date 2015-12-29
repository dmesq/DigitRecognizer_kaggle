import csv
import numpy as np
import json

def read_pixel_data(filename, nrows, flag):

	with open(filename, 'rt') as csvfile:
		''' flag: boolean, true if the data to read is the test set data (only 784 columns).
		          Otherwise false (when reading the training data - 785 columns)'''

		reader = csv.reader(csvfile)
		next(reader) #skip header row

		data = np.zeros( (nrows, 785), dtype=np.float64 )
		i = 0
		for row in reader:
			row_ints = [int(x) for x in row]

			if flag: row_ints = [1] + row_ints

			data[i, :] = row_ints
			i+=1

	return data

def read_json_object(filename):

	with open(filename, 'r') as f:
		data = json.load(f)

	return data

def write_json_object(data, filename):
	''' serializes the data as a json object in the file filename

		data: list
		filename: str, name of the file where to store the data'''

	with open(filename, 'w') as f:
		json.dump(data, f)

def write_predictions(data, filename):

	with open(filename, 'w') as csvfile:
		fieldnames = ['ImageId', 'Label']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

		writer.writeheader()

		for i, prediction in enumerate(data):
			writer.writerow({'ImageId': i+1, 'Label': prediction})

def parse_data(array, max_value):
	''' Changes original array
		Splits data into features and output.
		Adds a column of 1's to the feature array.'''

	Y = array[:, 0].copy()
	array[:, 0] = 1

	array = array / max_value

	return array, Y

def sigmoid(z):
	return 1 / ( 1 + np.exp(-z))





