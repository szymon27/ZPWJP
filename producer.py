import uuid

filename = "data.txt"
id = uuid.uuid4()
status = "pending"

with open(filename, 'a') as file:
    file.write(f'{id} {status}\n')
    print(f'save msg {id}')
