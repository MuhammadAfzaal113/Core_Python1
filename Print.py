class printer():
    categories = set()
    colors = set()
    size = set()
    value_list = list()
    sorted_list = list()
    filter_by = ("brand", "color", "price", "size")

    # Function to show values in table
    def table(self, values_of_list):
        print("No.,\t\tProduct Id,\t\tTitle")
        for x in values_of_list:
            print(x)
        values_of_list = values_of_list[:10]
        i = 0
        for p in values_of_list:
            i += 1
            print(i, " ", p[0], " ", p[2])
        return values_of_list

    # Function to show all values in file
    def row_show(self):
        for row in self.input_file:
            print(row)

    # Funtion to show Siz,Color,Categories in menu
    def set_show(self, values):
        if values!=None:
            i = 0
            for x in values:
                i += 1
                print(str(i) + " " + x)
            return True
        else:return False

    # Funtion to show detail of a single ID
    def whole_detail_of_id(self, inp,lists):
        print(lists[int(inp) - 1])
