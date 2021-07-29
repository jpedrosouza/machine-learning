import cv2
import matplotlib.pyplot as plt
import numpy as np
import os


def show_image(image):

    # Show image in window
    cv2.imshow('Image', image)

    cv2.waitKey(0)

    # Close all open windows
    cv2.destroyAllWindows()


def save_detect_faces(images, path):
    if not os.path.exists(path):
        os.mkdir(path)

    index = len(os.listdir(path))

    for image in images:
        cv2.imwrite(f"{path}/{index}.jpg", image)
        index += 1

def save_all_detect_faces_image(image, path):
     if not os.path.exists(path):
        os.mkdir(path)

     cv2.imwrite(f"{path}/detect_faces.jpg", image)   

def detect_faces(image_path: str):
    # Read image with OpenCv

    image = cv2.imread(image_path)

    type[image]

    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    features_haar = 'haarcascade_frontalface_alt2.xml'

    path = f"{cv2.haarcascades}/{features_haar}"

    classificator = cv2.CascadeClassifier(path)

    faces = classificator.detectMultiScale(grey_image)

    image_copy = np.array(image)

    for x, y, w, h in faces:
        cv2.rectangle(image_copy, (x, y), (x+w, y+h), (0, 255, 0), 2)

    crop_images = list()

    for x, y, w, h in faces:
        face = image[y:y+h, x:x+w]
        face = cv2.resize(face, (160, 160))
        crop_images.append(face)

    print('Number of faces', len(crop_images))

    save_detect_faces(crop_images, '../tmp')

    save_all_detect_faces_image(image_copy, '../tmp')
