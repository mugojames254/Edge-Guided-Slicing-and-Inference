
import cv2
import numpy as np


def edgeDensity(image):
    image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

    if image.shape[-1] == 4:
        image = image[:,:,:3]

    edges = cv2.Canny(image, threshold1=50, threshold2=150)
    normalized_edges = edges / 255

    edge_density = np.sum(normalized_edges) / (image.shape[0] * image.shape[1])

    if edge_density > 0.1:
        slice_height = image.shape[0] // 4
        slice_width = image.shape[1] // 4
        overlap_ratio = 0.4
    elif edge_density > 0.05:
        slice_height = image.shape[0] // 3
        slice_width = image.shape[1] // 3
        overlap_ratio = 0.3
    else:
        slice_height = image.shape[0] // 2
        slice_width = image.shape[1] // 2
        overlap_ratio = 0.2

    return slice_height, slice_width, overlap_ratio

