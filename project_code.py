import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('uav_image2.jpeg')
if img is None:
    print("Image not loaded ")
    exit()
img_color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges_normal = cv2.Canny(gray, 50, 150)
best_score = 0
best_low = 0
best_high = 0
fitness_history = []
for low in range(10, 100, 10):
    for high in range(100, 250, 10):
        edges = cv2.Canny(gray, low, high)
        score = np.sum(edges) - 0.4*np.std(edges)
        fitness_history.append(best_score)
        if score > best_score:
            best_score = score
            best_low = low
            best_high = high
print("Best thresholds:", best_low, best_high)
edges_best = cv2.Canny(gray, best_low, best_high)
plt.figure(figsize=(10,5))
plt.subplot(1,3,1)
plt.imshow(img_color)
plt.title("Original (Color)")
plt.subplot(1,3,2)
plt.imshow(edges_normal, cmap='gray')
plt.title("Normal")
plt.subplot(1,3,3)
plt.imshow(edges_best, cmap='gray')
plt.title("Optimized")
plt.show()
plt.plot(fitness_history)
plt.title("Fitness vs Iterations")
plt.xlabel("Iterations")
plt.ylabel("Fitness")
plt.show()