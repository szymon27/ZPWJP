import time

filename = "data.txt"


def get_index_of_first_pending_message():
    lines = []
    index = -1

    with open(filename, 'r') as file:
        lines = file.readlines()

    temp_index = 0
    found = False
    for line in lines:
        id = line.strip().split()[0]
        status = line.strip().split()[1]

        if status == "pending" and found is False:
            index = temp_index
            found = True

        temp_index = temp_index + 1

    return index


def process_message(index):
    lines = []

    with open(filename, 'r') as file:
        lines = file.readlines()

    id = lines[index].strip().split()[0]
    status = "in_progess"
    lines[index] = f'{id} {status}\n'

    with open(filename, 'w') as file:
        file.writelines(lines)

    print(f'start processing msg {id}')

    print(f'waiting...')
    time.sleep(3)

    with open(filename, 'r') as file:
        lines = file.readlines()

    id = lines[index].strip().split()[0]
    status = "done"
    lines[index] = f'{id} {status}\n'

    with open(filename, 'w') as file:
        file.writelines(lines)

    print(f'end processing msg {id}')


def do_work():
    index = get_index_of_first_pending_message()
    if index > -1:
        process_message(index)


while True:
    do_work()
    time.sleep(5)
