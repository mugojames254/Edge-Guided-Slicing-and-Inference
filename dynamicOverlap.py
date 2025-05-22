
import cv2
import numpy as np


def edgeDensity(image):
    image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

    edges = cv2.Canny(image, threshold1=50, threshold2=150)
    normalized_edges = edges / 255.0

    edge_density = np.mean(normalized_edges)
    
    img_height, img_width = image.shape
 
    if edge_density > 0.1:
        return img_height // 4, img_width // 4, 0.4
    elif edge_density > 0.05:
        return img_height // 3, img_width // 3, 0.3
    else:
        return img_height // 2, img_width // 2, 0.2
    
