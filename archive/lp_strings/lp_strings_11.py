# my_string = 'ABC'
# my_string = 'ABC123'
# my_string = 'ABC123!'

# print(my_string.isalpha())
# print(my_string.isalnum())

# my_string = '3'             # True - isdecimal(), isdigit(), isnumeric()
# my_string = '١٢٣٤٥٦٧٨٩'    # True - isdecimal(), isdigit(), isnumeric()
# my_string = '3²'            # True - isdigit(), isnumeric()
# my_string = '③'             # True - isdigit(), isnumeric()
my_string = 'Ⅻ'           # True - isnumeric()

print(my_string.isdecimal())
print(my_string.isdigit())
print(my_string.isnumeric())
