import os
from dynamicOverlap import edgeDensity

# from sahi.utils.ultralytics import (
#     download_yolov8n_model, download_yolov8n_seg_model
# )

from sahi import AutoDetectionModel
from sahi.utils.cv import read_image
from sahi.utils.file import download_from_url
from sahi.predict import get_prediction, get_sliced_prediction, predict
from IPython.display import Image

image_path = 'path/to/image.jpg'
yolov8_model_path = "path/to/model.pt"


detection_model = AutoDetectionModel.from_pretrained(
    model_type='yolov8',
    model_path=yolov8_model_path,
    confidence_threshold=0.3,
    device="cpu", # or 'cuda:0'
)


slice_height, slice_width, overlap_ratio = edgeDensity(image_path)

result = get_sliced_prediction(
    image_path,
    detection_model,
    slice_height = slice_height,
    slice_width = slice_width,
    overlap_height_ratio = overlap_ratio,
    overlap_width_ratio = overlap_ratio
)


object_count = len(result.object_prediction_list)

Image("demo_data/0.jpg")
