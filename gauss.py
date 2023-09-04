from matplotlib import pyplot as plt

number_in_the_group = int(input())


with open("laba1.txt", 'r') as read_data:  #read_data - ссылка на файл
    scanned_numbers = list(map(int, read_data.readlines())) #создание массива считанных данных
    print(len(scanned_numbers))
    
    if (len(scanned_numbers) % number_in_the_group) != 0:
        print("количество сканированных значений не делится на количество значений в группе")
    
  
grouped_numbers = [0 for _ in range(len(scanned_numbers) // number_in_the_group)]

number_in_group = 0

for scanned_number in range(0, len(scanned_numbers), number_in_the_group):
    grouped_numbers[scanned_number // number_in_the_group] += sum(scanned_numbers[scanned_number: scanned_number + number_in_the_group])
    
max_grouped_value = max(grouped_numbers) + 1

grouped_values = [0 for _ in range(max_grouped_value)]

for grouped_number in grouped_numbers:
    grouped_values[grouped_number] += 1

axis_x = []

for i, value in enumerate(grouped_values):
    
    axis_x.append(i)
    
    print(i , grouped_values[i])
    
    
bar = plt.bar(axis_x, grouped_values)

plt.show()