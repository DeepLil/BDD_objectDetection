# Dockerfile

# Use the official Python image as a base
FROM python:3.9

# Set the working directory
WORKDIR /app/dataAnalysis

# Copy the current directory contents into the container at /app/dataAnalysis
COPY . /app/dataAnalysis

# Install any required packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the scripts (you can customize this as needed)
#CMD ["python", "convert_to_yolo.py"]
