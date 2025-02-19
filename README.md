# Edge Guided Slicing

This project uses edge density to determine the slicing parameters for an image and performs object detection using a YOLOv8 model.

## Files

- `dynamicOverlap.py`: Contains the `edgeDensity` function which calculates the edge density of an image and determines the slicing parameters.
- `edge_guided_slicing.py`: Uses the `edgeDensity` function to get slicing parameters and performs object detection on the sliced image.

## Usage

1. Ensure you have all the required dependencies installed. You can install them using the `requirements.txt` file.
2. Update the `image_path` and `yolov8_model_path` variables in `edge_guided_slicing.py` with the path to your image and YOLOv8 model respectively.
3. Run the `edge_guided_slicing.py` script to perform object detection on the image.

## Citation
This project is part of the research paper:  

📄 **Njoroge J. Mugo, Ali Akbar, Lee Seojoon, Soonwook Kwon**  
*"Edge Guided Slicing and Inference (EGSI) with Feature Aggregation Network for Quantification of Large Defective Temporary Materials"*  
(Submitted to the *Journal of Asian Architecture and Building Engineering, 2025*)  


```sh
python edge_guided_slicing.py
