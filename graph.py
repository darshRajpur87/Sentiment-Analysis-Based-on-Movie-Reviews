import matplotlib.pyplot as plt
import numpy as np

# Model names and their respective metrics
models = ['SigSecure (CNN)', 'Siamese Network', 'SVM', 'Random Forest', 'Hybrid CNN-SVM']
accuracy = [83.0, 92.8, 85.6, 89.2, 95.2]
precision = [82.1, 91.5, 84.2, 88.0, 94.5]
recall = [82.6, 92.2, 85.0, 88.5, 94.8]
f1_score = [82.3, 91.8, 84.6, 88.2, 94.6]
far = [3.7, 3.8, 6.5, 4.2, 2.1]
frr = [4.0, 3.5, 6.8, 4.6, 2.3]

# Set bar width and positions
bar_width = 0.12
index = np.arange(len(models))

# Plotting
plt.figure(figsize=(14, 6))
plt.bar(index, accuracy, bar_width, label='Accuracy')
plt.bar(index + bar_width, precision, bar_width, label='Precision')
plt.bar(index + 2 * bar_width, recall, bar_width, label='Recall')
plt.bar(index + 3 * bar_width, f1_score, bar_width, label='F1-Score')
plt.bar(index + 4 * bar_width, far, bar_width, label='FAR')
plt.bar(index + 5 * bar_width, frr, bar_width, label='FRR')

# Chart formatting
plt.xlabel('Model')
plt.ylabel('Percentage')
plt.title('Performance Comparison of Signature Verification Models')
plt.xticks(index + 2.5 * bar_width, models, rotation=15)
plt.legend()
plt.tight_layout()

plt.grid(axis='y', linestyle='--', linewidth=0.5)
plt.show()
