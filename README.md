# BDD_objectDetection

Data Analysis:
1. Parse the labels from the json file into YOLO format (As I'm using Yolo varaint here)
2. Verify the labels by visualization
3. while verifying the number of lables vs corresponding images, there are differnces, so the labels without images or images without lables are removed. 
4. Observe the distribution of classes.
   It revealed long tail distribution as some classes are almost negligible compared to other classes. Also, observing the ratio of occuled/non occluded and truncated/non truncated ones to understand the percentage of hard examples in the data. Understanding the spatial distribution of each class using heatmap to identify anamolies like traffic light cannot be at bottom and car cannot be top. Plotting the aspect ratio of classes to identify anamoly in labelling. For example, person height should always be greater than width and vice versa for car. Though there may be a small percentage of outliers, we have to be sure the percentage is extremely small or negligible.

# No of instances per class

Training data:
<img width="1200" height="600" alt="bdd_distribution" src="https://github.com/user-attachments/assets/447fdfcf-953a-426f-beec-72a23f6322bf" />
Validation data:
<img width="1200" height="600" alt="bdd_distribution_val" src="https://github.com/user-attachments/assets/9ca4d65c-90fe-497a-a4a6-d3cfd2dc3f2f" />

# Spatial Distribution check

This spatial distribution is a health check to see the physical placement of the objects on the image. As the dataset is from a dashcam, it is natural to assume the road is in the middle center and all the vehicles are supposed to be on the road with a little variance. The traffic sign and traffic light are naturally assumed to be on the top left or right. This sanity check provides us with the placement and maybe the merit of the annotation too. 

Bike: Bicycle. Can be a parked one or one with a rider. In any way supposed to be at centre line with variance. As on road and on either side of the road. 
<img width="1000" height="600" alt="bike_heatmap" src="https://github.com/user-attachments/assets/296f6c98-bc48-4361-9afa-23b5dd74c587" />

This seems fine. 

Repeat with every class. 


<img width="1000" height="600" alt="bus_heatmap" src="https://github.com/user-attachments/assets/166b7eb7-16f2-4851-ac03-f67e1f8b079c" />

<img width="1000" height="600" alt="car_heatmap" src="https://github.com/user-attachments/assets/71575156-d816-454c-90e2-866f8441be23" />

<img width="1000" height="600" alt="motor_heatmap" src="https://github.com/user-attachments/assets/04b03512-fa7b-4ce9-87ea-9f6884a2b4c8" />

<img width="1000" height="600" alt="person_heatmap" src="https://github.com/user-attachments/assets/e6282ce2-b92a-4361-a336-58da121b5879" />

<img width="1000" height="600" alt="rider_heatmap" src="https://github.com/user-attachments/assets/0c3d6a18-98ce-4226-b0bc-6ac2927911fd" />

<img width="1000" height="600" alt="traffic light_heatmap" src="https://github.com/user-attachments/assets/bf71c3e1-c206-4378-942d-3e2f979db40d" />

<img width="1000" height="600" alt="traffic sign_heatmap" src="https://github.com/user-attachments/assets/57bc9fba-e251-44d3-af29-b3d431026b92" />

<img width="1000" height="600" alt="train_heatmap" src="https://github.com/user-attachments/assets/7403d9f7-b597-40ee-8327-5cc35d3226e0" />

<img width="1000" height="600" alt="truck_heatmap" src="https://github.com/user-attachments/assets/c5a32306-28e9-47e5-be5a-baa339fd9a66" />

# Dimension check

<img width="800" height="800" alt="bike_scatter" src="https://github.com/user-attachments/assets/44e92f94-8e18-4d1a-af5e-9eb6822e52a4" />

<img width="800" height="800" alt="bus_scatter" src="https://github.com/user-attachments/assets/56ee21a5-fe72-462c-b395-c14bd4d32081" />

<img width="800" height="800" alt="car_scatter" src="https://github.com/user-attachments/assets/1217e521-a8eb-4012-b5e7-da13c765b4d4" />

<img width="800" height="800" alt="motor_scatter" src="https://github.com/user-attachments/assets/c06b13b4-6114-4a6e-9f24-102dcd87c874" />

<img width="800" height="800" alt="person_scatter" src="https://github.com/user-attachments/assets/1c2dc6bf-59a7-4a45-b59f-24a5769ad239" />

<img width="800" height="800" alt="rider_scatter" src="https://github.com/user-attachments/assets/3c6af7fa-1be8-41c7-a6e7-394666ee3b32" />

<img width="800" height="800" alt="traffic light_scatter" src="https://github.com/user-attachments/assets/3d330b1e-1040-4178-b8d8-bd5ad75ff89e" />

<img width="800" height="800" alt="traffic sign_scatter" src="https://github.com/user-attachments/assets/21d28714-a17b-48f8-a3a3-26925c3da762" />

<img width="800" height="800" alt="train_scatter" src="https://github.com/user-attachments/assets/3f0e3378-a601-4cb0-808d-8327716dc7e9" />

<img width="800" height="800" alt="truck_scatter" src="https://github.com/user-attachments/assets/659a3241-ad94-4cbd-925d-2ef347545f9e" />










