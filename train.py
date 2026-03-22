from ultralytics import YOLO
def train_yolo_model(data_yaml, model_name="yolov8n.pt", epochs=11):
    # Load the model
    model = YOLO(model_name)
    
    # Train the model
    results = model.train(data=data_yaml, epochs=epochs, imgsz=640, resume = True, plots=True)

    return results

results = train_yolo_model("D:/Phani_Works/2025/Hailo/BDD/data.yaml", epochs=11)
