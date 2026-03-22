import json
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np


'''
Histogram of class distribution in the BDD100K dataset, along with percentages of occluded and truncated instances for each category.

'''

def analyze_bdd_distribution(json_path):
    print(f"Loading {json_path}...")
    with open(json_path, 'r') as f:
        data = json.load(f)

    
    stats = {}

    for entry in data:
        for lbl in entry.get('labels', []):
            cat = lbl['category'] 
            if cat in ['lane' , 'drivable area']:
                continue
            if cat not in stats:
                stats[cat] = Counter({'normal': 0, 'occ_only': 0, 'tru_only': 0, 'both': 0})
            
            attrs = lbl.get('attributes', {})
            is_occ = attrs.get('occluded', False)
            is_tru = attrs.get('truncated', False)

            if is_occ and is_tru:
                stats[cat]['both'] += 1
            elif is_occ:
                stats[cat]['occ_only'] += 1
            elif is_tru:
                stats[cat]['tru_only'] += 1
            else:
                stats[cat]['normal'] += 1

    # Sort categories by total volume
    categories = sorted(stats.keys(), key=lambda x: sum(stats[x].values()), reverse=True)
    
    # Extract data for plotting
    normal = np.array([stats[c]['normal'] for c in categories])
    occ_only = np.array([stats[c]['occ_only'] for c in categories])
    tru_only = np.array([stats[c]['tru_only'] for c in categories])
    both = np.array([stats[c]['both'] for c in categories])

    # Plotting
    plt.figure(figsize=(14, 8))
    
    
    p1 = plt.bar(categories, normal, color='#2ecc71', label='Normal (Clear)')
    p2 = plt.bar(categories, occ_only, bottom=normal, color='#3498db', label='Occluded Only')
    p3 = plt.bar(categories, tru_only, bottom=normal + occ_only, color='#f1c40f', label='Truncated Only')
    p4 = plt.bar(categories, both, bottom=normal + occ_only + tru_only, color='#e74c3c', label='Both (Occ + Tru)')

    plt.title("BDD100K Class Distribution with Visibility Attributes", fontsize=16, pad=20)
    plt.xlabel("Object Category", fontsize=12)
    plt.ylabel("Number of Instances", fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.legend(title="Visibility Status", frameon=True, loc='upper right')
    
    
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    
    
    for i, cat in enumerate(categories):
        total = normal[i] + occ_only[i] + tru_only[i] + both[i]
        occ_pct = ((occ_only[i] + both[i]) / total) * 100
        plt.text(i, total + (max(normal) * 0.02), f'{total}', ha='center', fontsize=9, fontweight='bold')

    plt.tight_layout()
    plt.savefig("bdd_distribution_refined.png", dpi=300)
    print("\nRefined chart saved as 'bdd_distribution_refined.png'")

