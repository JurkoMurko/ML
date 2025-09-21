import easyocr
import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image

PATH1 = "download.jpg"
PATH2 = "new2.jpg"
PATH3 = "IMG_6452.jpg"
PATH_card = "card.jpg"

reader = easyocr.Reader(['en'], gpu=True)
result = reader.readtext(PATH_card)

for i in result:
    print(i[1])
