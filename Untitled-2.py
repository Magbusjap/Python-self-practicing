"""# ex 9 - чтение файла в командной стрке
# Указываем путь к файлу
file_path = r"C:\Studying with C\IT disk C\Python self-practicing\sample read files\NEW_FILE.TXT"

# Открываем файл и читаем его содержимое
with open(file_path, 'r') as adv: # 'r' означает режим чтения (read)
    # Читаем все строки файла и выводим их на экран
    lines = adv.readlines()
    for line in lines:
        print(line.strip()) # strip() удаляет лишние пробелы и символы переноса строки"""




