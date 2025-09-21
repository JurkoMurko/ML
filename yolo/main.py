from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO("yolo11n.pt")

video_file_path = "C:/Users/jurko/Projects/Sky_Diving_Video_Project/Real2/GX010709.mp4"

# Run inference on the source
results = model(source=video_file_path, show=False, save=True)  # generator of Results objects
