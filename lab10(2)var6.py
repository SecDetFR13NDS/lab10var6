from pathlib import Path
if Path('input.txt').is_file() in '/C:':
    print ("Файл знайдено")
else:
    print ("Файл не знайдено")