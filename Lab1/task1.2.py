size = 1.44 * 1024 * 1024
count_of_pages = 100
count_of_lines = 50
count_of_symbols = 25
size_of_symbol = 4
size_of_book = size_of_symbol * count_of_symbols * count_of_lines * count_of_pages
count_of_book = size // size_of_book
print(f"Количество книг, помещающихся на дискету: {count_of_book:.0f}")
