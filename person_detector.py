import cv2


def person_count(file_path):
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    img = cv2.imread(f'{file_path}')
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    boxes, weights = hog.detectMultiScale(gray, winStride=(8, 8))

    # import numpy as np
    # boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
    # for (xA, yA, xB, yB) in boxes:
    #     cv2.rectangle(img, (xA, yA), (xB, yB), (0, 255, 0), 2)
    # cv2.imshow('img', img)
    # cv2.waitKey()

    return (len(boxes))
