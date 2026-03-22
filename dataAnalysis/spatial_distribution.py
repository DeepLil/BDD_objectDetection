from collections import defaultdict
import numpy as np
import json
import os
import matplotlib.pyplot as plt

'''
plot the spatial distribution of objects and dimension analysis of bounding boxes

'''

def analyze_patterns(json_path, output_dir="analysis_results"):
    os.makedirs(output_dir, exist_ok=True)
    
    with open(json_path, 'r') as f:
        data = json.load(f)

    # Data structures for analysis
    spatial_data = defaultdict(list)  # (x_center, y_center)
    dimension_data = defaultdict(list) # (width, height)
    anomalies = []

    img_w, img_h = 1280, 720

    for entry in data:
        for lbl in entry.get('labels', []):
            if 'box2d' not in lbl: continue
            
            cat = lbl['category']
            box = lbl['box2d']
            
            # 1. Normalize and find centers
            w_box = (box['x2'] - box['x1'])
            h_box = (box['y2'] - box['y1'])
            xc = (box['x1'] + box['x2']) / 2
            yc = (box['y1'] + box['y2']) / 2
            
            spatial_data[cat].append((xc, yc))
            dimension_data[cat].append((w_box, h_box))

        

    # Heatmaps
    for cat in spatial_data:
        coords = np.array(spatial_data[cat])
        plt.figure(figsize=(10, 6))
        plt.hist2d(coords[:, 0], coords[:, 1], bins=50, cmap='hot', range=[[0, 1280], [0, 720]])
        plt.colorbar(label='Frequency')
        plt.title(f"Spatial Distribution Heatmap: {cat}")
        plt.gca().invert_yaxis() # Image coordinates start at top-left
        #plt.savefig(f"{output_dir}/{cat}_heatmap.png")
        plt.close()

    #  Scatter Plots
    for cat in dimension_data:
        dims = np.array(dimension_data[cat])
        plt.figure(figsize=(8, 8))
        plt.scatter(dims[:, 0], dims[:, 1], alpha=0.3, s=1)
        plt.title(f"Width vs Height Distribution: {cat}")
        plt.xlabel("Width (pixels)")
        plt.ylabel("Height (pixels)")
        plt.grid(True)
        #plt.savefig(f"{output_dir}/{cat}_scatter.png")
        plt.close()

    

