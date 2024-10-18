import cv2
import numpy as np
import os
import math

def correct_orientation(input_data, qr_size, module_size):
    new_coords = []
    for coords, state in input_data:
        x = coords[0]
        y = qr_size - coords[1]
        new_coords.append(((x, y), state))
    return new_coords

def write_image(image, file_dir):
    if file_dir is None:
        cv2.imwrite('qr_image.png', image)
    else:
        try:
            cv2.imwrite(file_dir, image)
        except:
            raise ValueError(f"{file_dir} Does Not Exist")

def create_qr_png(input_data, file_dir, code_shape='Square'):
    qr_size = int(math.sqrt(len(input_data)))
    module_size = 1
    size_factor = 80
    placement = 100
    oriented_data = correct_orientation(input_data, qr_size, module_size)
    width = (qr_size * size_factor) + (placement * 2)
    height = width
    qr_image = np.zeros([width+(module_size*size_factor)+placement, height, 3],dtype=np.uint8)
    qr_image.fill(255)

    for coords, state in oriented_data:
        x, y = coords
        x1 = x * size_factor + placement - 50
        y1 = y * size_factor + placement
        x2 = (x + 1) * size_factor + placement - 50
        y2 = (y + 1) * size_factor + placement
        if state == 0:
            pass
        else:
            color = (0, 0, 0)
            if code_shape == 'Circle':
                cv2.circle(qr_image, (x1 + (x2 - x1), y1 + (y2 - y1)), 40, color, thickness=-1)
            else:
                cv2.rectangle(qr_image, (x1 + 50, y1), (x2 + 50, y2), color, -1)

    bigger = cv2.resize(qr_image, (250, 250))
    write_image(bigger, file_dir)

def display_qr_image(input_data, code_shape):
    alignment_data = []
    module_size = 1
    size_factor = 80
    qr_size = int(math.sqrt(len(input_data)))
    placement = 100
    oriented_data = correct_orientation(input_data, qr_size, module_size)
    oriented_alignment = correct_orientation(alignment_data, qr_size, module_size)
    width = (qr_size * size_factor) + (placement * 2)
    height = width
    qr_image = np.zeros([width+(module_size*size_factor)+placement, height, 3],dtype=np.uint8)
    qr_image.fill(255)

    for coords, state in oriented_data:
        x, y = coords
        x1 = x * size_factor + placement - 50
        y1 = y * size_factor + placement
        x2 = (x + 1) * size_factor + placement - 50
        y2 = (y + 1) * size_factor + placement
        if state == 0:
            pass
        else:
            if coords in [i[0] for i in oriented_alignment]:
                color = (0, 255, 0)
            else:
                color = (0, 0, 0)

            if code_shape == 'Circle':
                cv2.circle(qr_image, (x1+(x2-x1), y1+(y2-y1)), 40, color, thickness=-1)
            else:
                cv2.rectangle(qr_image, (x1 + 50, y1), (x2 + 50, y2), color, -1)

    cv2.imshow('QR', cv2.resize(qr_image, (600, 600)))
    cv2.waitKey(0)
