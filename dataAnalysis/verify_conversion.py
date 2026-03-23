import cv2
import random
import os

''' 
verify the labels produced by the conversion script by drawing the bounding boxes on the images.
Input: image_dir: directory containing the images, label_dir: directory containing the YOLO format labels.
Output: Displays a random image with the bounding boxes drawn on it.
'''

class verifyConversion:
    def __init__(self, image_dir, label_dir):
        self.image_dir = image_dir
        self.label_dir = label_dir

    def verify_conversion(self):
        # Pick a random image
        image_files = [f for f in os.listdir(self.image_dir) if f.endswith(('.jpg', '.png'))]
        img_name = random.choice(image_files)
        
        # Load image
        img_path = os.path.join(self.image_dir, img_name)
        image = cv2.imread(img_path)
        h, w, _ = image.shape
        
        # Load corresponding label
        label_path = os.path.join(self.label_dir, img_name.replace('.jpg', '.txt').replace('.png', '.txt'))
        
        if not os.path.exists(label_path):
            print(f"Label not found for {img_name}")
            return
    
        with open(label_path, 'r') as f:
            lines = f.readlines()
            
        for line in lines:
            parts = line.split()
            class_id = parts[0]
            # De-normalize coordinates
            x_c, y_c, wb, hb = map(float, parts[1:])
            
            # Convert from center-format to corner-format for OpenCV
            x1 = int((x_c - wb/2) * w)
            y1 = int((y_c - hb/2) * h)
            x2 = int((x_c + wb/2) * w)
            y2 = int((y_c + hb/2) * h)
            
            # Draw the box
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, f"ID: {class_id}", (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Verification", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
