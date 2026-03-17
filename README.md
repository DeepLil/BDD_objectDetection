# BDD_objectDetection

Data Analysis:
1. Parse the labels from the json file into YOLO format (As I'm using Yolo varaint here)
2. Verify the labels by visualization
3. Observe the distribution of classes.
   It revealed long tail distribution as some classes are almost negligible compared to other classes. Also, observing the ratio of occuled/non occluded and truncated/non truncated ones to understand the percentage of hard examples in the data. Understanding the spatial distribution of each class using heatmap to identify anamolies like traffic light cannot be at bottom and car cannot be top. Plotting the aspect ratio of classes to identify anamoly in labelling. For example, person height should always be greater than width and vice versa for car. Though there may be a small percentage of outliers, we have to be sure the percentage is extremely small or negligible.
