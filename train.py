from ultralytics import YOLO
def train_yolo_model(data_yaml, model_name, epochs):
    # Load the model
    model = YOLO(model_name)
    
    # Train the model
    results = model.train(data=data_yaml, epochs=epochs, imgsz=640, resume = True, plots=True)

    return results

results = train_yolo_model("data.yaml", "best.pt", epochs=11)
