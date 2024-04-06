import sys

if len(sys.argv) != 2:
    print("Usage: python process_image.py <image_path>")
    sys.exit(1)

filepath = sys.argv[1]

#image processing code goes here
import cv2
import numpy as np

def finetune(image):
    image = cv2.resize(image, None, fx=0.5,fy=0.5)
    cv2.imshow("Img", image)
    cv2.waitKey(0)

    image_array = np.array(image)
    image_array[image_array < 50] = 0
    image_array[image_array >= 50] = 255

    cv2.imshow("Finetuned Image",image_array)

    return image_array

def edgeDetection(image):
    # Detecting edges
    edges = cv2.Canny(image, 255, 255)

    cv2.imshow("Edges", edges)
    cv2.waitKey(0)

    return edges


def contourDetection(image,edges):
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Creating an empty image to draw contours
    contour_image = np.zeros_like(image, dtype=np.uint8)
    
    # Calculating contour lengths
    contour_lengths = [cv2.arcLength(contour, closed=False) for contour in contours]

    # Find the index of the contour with the maximum length
    max_length_index = np.argmax(contour_lengths)

    # print(max_length_index) 

    # Draw the longest contour on the empty image
    cv2.drawContours(contour_image, contours, max_length_index, (255, 255, 255), 2)

    # Display the result
    cv2.imshow('Longest Contour', contour_image)
    cv2.waitKey(0)

    return contour_image


def selectRequisties(filepath):

    requisties_tulip = [160,200,350,430,510,600]
    requisties_sp = [80,160,210,235,430]
    requisties_t = [343,470,540]

    if('spotlight' in filepath):
        return requisties_sp
    elif('tulip' in filepath):
        return requisties_tulip
    else:
        return requisties_t


def proposed_alg(image,contour_image,requisties):
    contour_array = np.array(contour_image)

    for row in range(0, contour_array.shape[0]):
        # Find the indices of white pixels in the row
        white_pixel_indices = np.where(contour_array[row] == 255)[0]

        # Check if there are continuous white pixels
        if (row in requisties) and len(white_pixel_indices) > 0 :
            # Measure the length until another set of white pixels is encountered
            start_position = white_pixel_indices[0]
            end_position = white_pixel_indices[-1]

            # Calculate the length
            length = end_position - start_position

            # Draw a line indicating the length
            cv2.line(image, (start_position, row), (end_position, row), (255, 255, 255), 2)

            # Adding text indicating the length with defined color
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(image, f'Length {row}: {length}px', (start_position, row - 10), font, 0.5, (255,255,255), 2)

            print(f"Length: {length}px")
    
    return image


def display(image):
    cv2.imshow('Contours with Lengths', image)
    cv2.waitKey(0)


image = cv2.imread(filepath)

image = finetune(image)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = edgeDetection(image)

contour_image = contourDetection(image,edges)


requisties = selectRequisties(filepath)

image = proposed_alg(image,contour_image,requisties)

display(image)

cv2.destroyAllWindows()

print(f"Processing image: {image_path}")



