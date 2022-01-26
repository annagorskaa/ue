import os
from Detector import detection


def show_data():

    path = 'pictures/'
    data_format = ['.jpg']

    for (path, dirs, data) in os.walk(path):
        for pic in data:
            if pic.endswith(tuple(data_format)):
                print(pic)
                photo = path + pic
                detection(photo)
