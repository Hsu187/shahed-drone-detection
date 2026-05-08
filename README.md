# shahed-drone-detection
Computer vision Model to detect shahed fixed wing drone. 


## Data Base
Collected images and annotation in roboflow. Data set link: https://app.roboflow.com/hsu-myat-thein-lwin/shahed_fixedwingdrone_detection/7. More than 1000 images: different weather conditions, environment, angles and distance, use Bounding box for annotation (.zip file also in file). Argumentations used-
1. Mosaic (0.909) - Combined 4 training images into one
2. Rotation (±1.11°) - Simulated drone banking angles
3. Scale (0.562) - Simulated drones at varying distances
4. Horizontal Flip (0.5) - 50% random horizontal flip
5. Brightness (±56.6%) - Handled different lighting conditions
6. Saturation (±64.5%) - Color intensity variation
7. Hue (±1.4%) - Minor color shifts
8. Translation (±10%) - Drones near frame edges
9. Close Mosaic (10) - Disabled mosaic in final 10 epochs
Dataset yoloV26 format and trained in Google colab

## Result
mAP50: 0.980  
mAP50-95: 0.843   
FPS: 73.7 (Real-time)
