from PIL import Image
from os import listdir
import cv2

def load_images(path):

    imagesList = listdir(path)
    loadedImages = []
    for image in imagesList:
        img = cv2.imread(path + image)
        loadedImages.append(img)

    return loadedImages

def load_results(path):
    imagesList = listdir(path)
    loadedImages = []
    for image in imagesList:
        img = Image.open(path + image)
        loadedImages.append(img)

    return loadedImages


def load_image(path):
    return cv2.imread(path)
