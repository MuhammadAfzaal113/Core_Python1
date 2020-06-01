import csv


class file_reader:
    input_file = dict()

    def file_reader(self):
        # Constructor
        self.input_file = csv.DictReader(open("products.csv"))
        return self.input_file
