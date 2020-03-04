# from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2

def generateHenonMap(image_size):
    x = 0.293201174303193
    y = 0.293201174303193
    [w, h, d] = image_size
    sequence_size = w * h * 8
    bit_sequence = [] #array contains 8 bits
    byte_array = []
    for i in range(sequence_size):
        #Henon map formula
        xN = y + 1 - 1.4 * x**2
        yN = 0.3 * x
        
        #xN and yN becomes the new x and y
        x = xN
        y = yN

        #Convert to binary using the threshold value
        if xN <= 0.3992:
            bit = 0
        else:
            bit = 1
        #insert bit to bit_sequence
        try:
            # bit_sequence = np.append(bit_sequence, bit)
            bit_sequence.append(bit)
        except:
            bit_sequence = [bit]
        # convert to decimal
        if i % 8 == 7:
            decimal = dec(bit_sequence)
            try:
                # byte_array = np.append(byte_array, decimal)
                byte_array.append(decimal)
            except:
                byte_array = [decimal]
            bit_sequence = []
    byte_array = np.asarray(byte_array)
    henon_map = np.reshape(byte_array, [w, h])
    return henon_map

def dec(bitSequence):
    decimal = 0
    for bit in bitSequence:
        decimal = decimal * 2 + int(bit)
    return decimal