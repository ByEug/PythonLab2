import random
import tempfile


def sort_into_one_file(files_list):
    a_list = files_list[0]
    b_list = files_list[1]
    print(a_list.readline())
    print(b_list.readline())
    counter = 2
    while counter < 5:
        file_buff = tempfile.NamedTemporaryFile(mode='w+', delete=False, prefix='lab2')
        a_min = int(a_list.readline())
        b_min = int(b_list.readline())
        while True:
            if a_min >= b_min:
                file_buff.write(str(b_min) + '\n')
                buff = b_list.readline()
                if len(buff) != 0:
                    b_min = int(buff)
                else:
                    break
            else:
                file_buff.write(str(a_min) + '\n')
                buff = a_list.readline()
                if len(buff) != 0:
                    a_min = int(buff)
                else:
                    break
        if len(a_list.readline()) == 0:
            buffer = b_list.readline()
            while len(buffer) != 0:
                file_buff.write(buffer + '\n')
                buffer = b_list.readline()
        if len(b_list.readline()) == 0:
            buffer = a_list.readline()
            while len(buffer) != 0:
                file_buff.write(buffer + '\n')
                buffer = a_list.readline()
        file_buff.seek(0)
        a_list = file_buff
        b_list = files_list[counter]
        print(a_list.readline())
        print(b_list.readline())
        counter += 1
    with open('sorted_numbers.txt', 'w') as f:
        f.writelines(a_list.read())


def merge_sort(numbers):
    if len(numbers) > 1:
        center_number = len(numbers) // 2
        left_part = numbers[:center_number]
        right_part = numbers[center_number:]
        merge_sort(left_part)
        merge_sort(right_part)
        count_lp = count_rp = count_list = 0
        while count_lp < len(left_part) and count_rp < len(right_part):
            if left_part[count_lp] <= right_part[count_rp]:
                numbers[count_list] = left_part[count_lp]
                count_lp += 1
                count_list += 1
            else:
                numbers[count_list] = right_part[count_rp]
                count_rp += 1
                count_list += 1
        while count_lp < len(left_part):
            numbers[count_list] = left_part[count_lp]
            count_lp += 1
            count_list += 1
        while count_rp < len(right_part):
            numbers[count_list] = right_part[count_rp]
            count_rp += 1
            count_list += 1


amount = 5000000
with open('numbers.txt', 'w') as file:
    file.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(amount))
names_list = []

with open('numbers.txt', 'r') as file:
    i = 0
    j = 0
    size_buff = 1000000
    while j < amount / size_buff:
        f1 = tempfile.NamedTemporaryFile(mode='w+b', delete=False, prefix='lab2')
        names_list.append(f1.name)
        while i < size_buff:
            bytes_line = str.encode(file.readline())
            f1.write(bytes_line)
            i += 1
        i = 0
        j += 1

for file_name in names_list:
    file = open(file_name)
    list_to_sort = []
    for line in file:
        list_to_sort.append(int(line))
    merge_sort(list_to_sort)
    file.close()
    file = open(file_name, 'w')
    for item in list_to_sort:
        file.write(str(item) + '\n')
    file.close()


files = []
i = 1
for filename in names_list:
    file = open(filename)
    files.append(file)
sort_into_one_file(files)
