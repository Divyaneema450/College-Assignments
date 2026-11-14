
# Assignment No. 8
# Binary Classification using Logistic Regression

# Import Libraries
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    roc_curve,
    roc_auc_score
)

# Step 1: Load Breast Cancer Dataset
data = load_breast_cancer()

X = data.data
y = data.target

print("Breast Cancer Dataset Loaded Successfully")
print("Dataset Shape:", X.shape)
print("Target Classes:", data.target_names)
print()

# Step 2: Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))
print()

# Step 3: Train Logistic Regression Model
model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=10000)
)

model.fit(X_train, y_train)

print("Logistic Regression Model Trained Successfully")
print()

# Step 4: Make Predictions
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# Step 5: Calculate Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", round(accuracy * 100, 2), "%")
print()

# Step 6: Display Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:")
print(cm)
print()

# Save Confusion Matrix Graph
display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=data.target_names
)

display.plot(cmap="Blues")
plt.title("Confusion Matrix")
plt.savefig("confusion_matrix.png")
plt.show()

# Step 7: Plot ROC Curve and Calculate AUC
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
auc = roc_auc_score(y_test, y_prob)

print("ROC AUC Score:", round(auc, 4))

plt.figure()
plt.plot(fpr, tpr, label=f"ROC Curve (AUC = {auc:.4f})")
plt.plot([0, 1], [0, 1], linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.savefig("roc_curve.png")
plt.show()

print("Evaluation Completed Successfully")
