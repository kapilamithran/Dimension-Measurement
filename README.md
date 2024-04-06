# Dimension-Measurement
A new algorithm utilizes a high-res Pi camera with Raspberry Pi 3 for edge detection in a controlled environment, ensuring precise part detection and measurement. With an accuracy of 88.48/93.50% in dimension measurements, it enhances manufacturing tool and component quality, boosting production efficiency.

The dimension measurement process comprises five stages: binary conversion, edge detection, contour detection, dimension measurement, and output display. Binary conversion transforms the image into binary format, distinguishing tool area (black, value 0) from surroundings (white, value 255). Edge detection, utilizing the Laplacian algorithm, identifies tool boundaries. Contours are then extracted, with the largest contour selected. Finally, dimensions are determined based on the tool in use.
app.py -> run
process_image.py -> proposed algorithm
uploads -> input images
templates -> HTML source code
