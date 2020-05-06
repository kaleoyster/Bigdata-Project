"""
description: data cleaning and processing script
"""

from csv import reader



def load_csv(filename):
    """
    args: csv filename
    extracts row from the dataset and return m x n list
    """
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)

    return dataset

def convert_to_int(dataset, index):
    """
    args: dataset(list), index (list)
    returns: dataset(list)
    converts string values to string in the dataset
    """
    for row in dataset[1:]:
        row[index] = float(row[index].strip())
    return dataset

def cols_to_int(dataset, cols):
    """
    args: dataset(list), cols (list)
    returns: dataset(list)
    converts string values to string in the dataset
    """  
    for col in cols:
        dataset = convert_to_int(dataset, col)
    return dataset

def training(training_data):
    pass


def main():

    # Read csv file
    dataset = load_csv('data/complete.csv')
    header = dataset[0]
    
    # Convert string to int
    dataset = cols_to_int(dataset, [2, 3, 4, 5, 6, 7, 8])

    # Removing null values and cleaning
    print(dataset[1:5])


if __name__ =='__main__':
    main()

