from Read_File import file_reader
from Print import printer
from Manager import manage_class
from User_Input import user_input_class


lists = list()
reader = file_reader()
user_input = user_input_class()
display = printer()
manage = manage_class()
input_file = reader.file_reader()
categories = manage.display_categories(input_file)
display.set_show(categories)
categories = user_input.category_input(categories)
print(categories)
a = str(user_input.filter_via())  # a=color,size etc
selected_filtered_value = manage.for_categories(categories, a)  # selected filter values = details of color/size etc

if selected_filtered_value is not None and selected_filtered_value is not "price":
    if display.set_show(selected_filtered_value):
        lists = manage.filter_for_color_size(categories, manage.check_filtering_method(a, selected_filtered_value), a,
                                             size_color_checker=True)
        lists = display.table(manage.proceeding_menu_checker(user_input.table_menu(), lists))
        display.whole_detail_of_id(user_input.id_selector(), lists)
    else:
        print("Nothing Found")

elif selected_filtered_value == "price":
    minimum_price = input("Enter minimum Price: ")
    maximum_price = input("Enter maximum Price: ")
    lists = manage.filter_for_color_size(categories, _min_price=minimum_price, _max_price=maximum_price,
                                         size_color_checker=True)
    lists = display.table(manage.proceeding_menu_checker(user_input.table_menu(), lists))
    display.whole_detail_of_id(user_input.id_selector(), lists)
else:
    print("There is no product in this filtering")
# self.proceeding_menu_checker(inp)
