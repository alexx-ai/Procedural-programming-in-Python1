import math

# Параметры книги
pages = 100
rows_per_page = 50
symbols_per_row = 25
bytes_per_symbol = 4

# Объем дискеты
disk_size_mb = 1.44
disk_size_bytes = disk_size_mb * 1024 * 1024  # Перевод из Мб в байты

# Вычисление объема одной книги
book_size_bytes = pages * rows_per_page * symbols_per_row * bytes_per_symbol

# Вычисление количества книг на дискете
books_on_disk = math.floor(disk_size_bytes / book_size_bytes)  # Округление вниз
print("Количество книг, помещающихся на дискету:", books_on_disk)