import requests
import uuid
import os


base_path = './images'
image_ext = 'jpg'


def save_image(content):
    new_file_name = f'{uuid.uuid4()}.{image_ext}'
    with open(f'{base_path}/{new_file_name}', 'wb') as file:
        file.write(content)
    return f'{base_path}/{new_file_name}'


def get_image(url):
    response = requests.get(url)
    response.raise_for_status()
    return save_image(response.content)


def remove_file(file_path):
    os.remove(file_path)
