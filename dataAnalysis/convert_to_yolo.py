
import json
import os
from pathlib import Path
from tqdm import tqdm


''' 
Converting the json annotations to YOLO format . 
Input: Takes label path json_path
Output: creates a .txt file for each image abd stores the labels in YOLO format in output_dir. output_dir should be in the same directory as the images.
'''
class BDDToYOLOConverter:
    def __init__(self, json_path, output_dir, img_w=1280, img_h=720):
        self.json_path = json_path
        self.output_dir = Path(output_dir)
        self.label_dir = self.output_dir
        self.img_w = img_w
        self.img_h = img_h
        
        # BDD100K Official Classes
        self.category_map = {
            "person": 0, "rider": 1, "car": 2, "truck": 3, 
            "bus": 4, "train": 5, "motor": 6, "bike": 7, 
            "traffic light": 8, "traffic sign": 9
        }
        
        self.label_dir.mkdir(parents=True, exist_ok=True)

    def normalize_bbox(self, box):
        """Converts [x1, y1, x2, y2] to [x_center, y_center, w, h] normalized."""
        dw = 1.0 / self.img_w
        dh = 1.0 / self.img_h
        
        x_center = (box['x1'] + box['x2']) / 2.0
        y_center = (box['y1'] + box['y2']) / 2.0
        w = box['x2'] - box['x1']
        h = box['y2'] - box['y1']
        
        return (x_center * dw, y_center * dh, w * dw, h * dh)

    def convert(self):
        print(f"Loading {self.json_path}...")
        with open(self.json_path, 'r') as f:
            data = json.load(f)

        for entry in tqdm(data, desc="Converting BDD to YOLO"):
            image_name = entry['name']
            label_file = self.label_dir / f"{Path(image_name).stem}.txt"
            
            yolo_lines = []
            for lbl in entry.get('labels', []):
                if 'box2d' not in lbl:
                    continue
                
                cat = lbl['category']
                if cat not in self.category_map:
                    continue
                
                class_id = self.category_map[cat]
                norm_box = self.normalize_bbox(lbl['box2d'])
                
                # Format: class_id x_center y_center width height
                line = f"{class_id} " + " ".join([f"{x:.6f}" for x in norm_box])
                yolo_lines.append(line)

            with open(label_file, 'w') as f:
                f.write("\n".join(yolo_lines))
