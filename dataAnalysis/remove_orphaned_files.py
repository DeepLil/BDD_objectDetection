

import os


''' 

there may be some image files that do not have a corresponding label file. This function removes those orphaned image files.

'''

def remove_orphaned_files(image_dir, label_dir):
    label_files = set()
    for label_file in os.listdir(label_dir):
        if label_file.endswith(('.txt')):
            label_files.add(os.path.splitext(label_file)[0])

    print(f"Found {len(label_files)} image files in {label_dir}")

    # Iterate through image files and remove those without a corresponding label
    removed_count = 0
    for image_file in os.listdir(image_dir):
        if image_file.endswith('.jpg'): 
            image_base_name = os.path.splitext(image_file)[0]
            if image_base_name not in label_files:
                image_path = os.path.join(image_dir, image_file)
                try:
                    os.remove(image_path)
                    print(f"Removed orphan label file: {image_file}")
                    removed_count += 1
                except OSError as e:
                    print(f"Error removing {image_file}: {e}")

    print(f"Finished cleaning labels. Removed {removed_count} orphan image files.")