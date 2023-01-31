
def write_data_student(data):
    with open('Student_Directory.txt', 'a', encoding='utf-8') as file:
        file.write(f"\n{';'.join(data)}")

def write_data_class(data):
    with open('Class_Directory.txt', 'a', encoding='utf-8') as file:
        file.write(f"\n{';'.join(data)}")

def search_data(word, data):
    if len(data) > 0:
        for item in data:
            if word in item:
                return item
    else:
        return None

def get_all_students():
    with open('Student_Directory.txt', 'r', encoding='utf-8') as file:
        data = []
        for line in file:
            temp = line.strip().split(';')
            data.append(temp)
    return data

def get_all_classes():
    with open('Class_Directory.txt', 'r', encoding='utf-8') as file:
        data = []
        for line in file:
            temp = line.strip().split(';')
            data.append(temp)
    return data

def get_student_id():
    with open('last_id.txt', 'r', encoding='utf-8') as file:
        id = file.read()
        id = int(id) + 1

    with open ('last_id.txt', 'w', encoding='utf-8') as file:
        file.write(str(id))

    return str(id)
