from ultralytics import YOLO
def val_yolo_model(data_yaml, model_path):
    # Load the model
    model = YOLO(model_path)
    
    # Train the model
    results = model.val(data=data_yaml)

    return results

results = val_yolo_model("data.yaml")
