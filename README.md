 
#  Color Image Edge Detection using Optimized Thresholding (WOA)
**overview:**
This project implements **edge detection on color images** using an optimization-based approach inspired by the **Whale Optimization Algorithm (WOA)**.
Unlike traditional methods that use fixed threshold values, this project finds **optimal thresholds automatically**, resulting in improved edge clarity and reduced noise.

## Features
- Edge detection using OpenCV (Canny)
- Optimization of thresholds (WOA-inspired search)
- Improved edge quality over fixed methods
- Visualization using Matplotlib
- Fitness tracking across iterations

## Technologies Used
- Python  
- NumPy  
- OpenCV  
- Matplotlib  

## Methodology

1. Load input color image  
2. Convert image to grayscale  
3. Apply standard Canny edge detection  
4. Iterate through multiple threshold values  
5. Evaluate each using a fitness function  
6. Select best thresholds  
7. Generate optimized edge output  

 
##  Optimization Strategy
The fitness function used:
Fitness = Sum of edges − (0.4 × Standard Deviation)
This ensures:
- Maximum edge detection  
- Minimum noise
- 

## Results
- **Normal Canny Output:** Uses fixed thresholds  
- **Optimized Output:** Better edges with less noise  
Also includes:
- Fitness vs Iterations graph  

## How to Run
1. Install dependencies:
pip install opencv-python numpy matplotlib
