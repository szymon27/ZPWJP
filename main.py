from typing import Union
from fastapi import FastAPI, UploadFile
from person_detector import person_count
from utils import get_image, remove_file, save_image


app = FastAPI()


@app.get("/disk")
def person_count_from_disk(file_path='./images/img1.jpg'):
    return person_count(file_path)


@app.get("/url")
def person_count_from_url(url):
    img_path = get_image(url)
    count = person_count(img_path)
    remove_file(img_path)
    return count


@app.post("/img")
async def person_count_from_image(image: UploadFile):
    img_path = save_image(await image.read())
    count = person_count(img_path)
    remove_file(img_path)
    return count
