import csv
from collections import defaultdict


def display_category():
    # open csv file and after pickup category column in list make it set to remove redundancy

    columns = defaultdict(list)  # each value in each column is appended to a list

    with open('products.csv' , 'r') as source_file:
        source_file_reader = csv.DictReader(source_file)  # read rows into a dictionary format
        for row in source_file_reader:  # read a row as {column1: value1, column2: value2,...}
            for (k, v) in row.items():  # go over each column name and value
                columns[k].append(v)  # append the value into the appropriate list based on column name k

    category_list = columns['category']  # pick the category column
    category_set = set(category_list)  # convert into set to remove redundancy
    joined_list_of_category = [str(s) for s in category_set]  # convert the set into string to print the output
    # without curly braces
    joined_list_of_category.sort()
    joined_string = ", ".join(joined_list_of_category)  # put the comma between strings(categories)

    print(joined_string, "\n")


def search_category():
    with open('products.csv', 'r') as source_file:
        category = input('Select category : ')
        source_file_reader = csv.reader(source_file)
        for row in source_file_reader:
            if row[2] == category:
                print(row, "\n")
