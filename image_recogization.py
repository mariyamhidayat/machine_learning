
from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

# Run inference on an image
results = model(source='C:\\Users\Swan Computers\\.vscode\extensions\\img1.jpg',show=True,conf=0.5,save=True) 



# View results