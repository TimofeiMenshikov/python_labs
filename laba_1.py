

with open("laba1.txt", 'r') as read_data:  #read_data - ссылка на файл
    scanned_numbers = list(map(int, read_data.readlines())) #создание массива считанных данных
    
    max_value = max(scanned_numbers) + 1 # находим максимальное значение для массива значений. добавляем 1, так как range без верхней границы
    
    values = [0 for _ in range(max_value)] # создаем массив , где адрес очередной ячейки массива - одно из возможных значений, а в самой ячейке - количество встречаемых значений
    
    for scanned_number in scanned_numbers:  #цикл по массиву считанных данных
        values[scanned_number] += 1      #обращаемся к ячейке массива и увеличиваем на 1 кол-во встречаемых чисел, равных данному        
    
    

    
    
    


