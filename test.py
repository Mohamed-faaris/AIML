import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score 
from sklearn.tree import plot_tree 
# Step 1: Load Iris dataset 
iris = load_iris() 
X = iris.data 
y = iris.target 
feature_names = iris.feature_names 
target_names = iris.target_names 
# Step 2: Split data into train and test sets 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) 
# Step 3: Create and train the Random Forest model 
rf_model = RandomForestClassifier(n_estimators=5, random_state=42) 
rf_model.fit(X_train, y_train) 
# Step 4: Predict and evaluate 
y_pred = rf_model.predict(X_test) 
accuracy = accuracy_score(y_test, y_pred) 
print("Random Forest Accuracy:", accuracy) 
# Step 5: Feature importance 
importances = rf_model.feature_importances_ 
print("\nFeature Importances:") 
for name, importance in zip(feature_names, importances): 
    print(f"{name}: {importance:.4f}") 
# Step 6: Visualize a few trees in the forest 
plt.figure(figsize=(15, 10)) 
for i in range(3):  # Display first 3 trees 
    plt.subplot(1, 3, i + 1) 
plot_tree(rf_model.estimators_[i], 
feature_names=feature_names, 
class_names=target_names, 
filled=True, 
rounded=True, 
fontsize=6) 
plt.title(f"Tree {i+1}") 
plt.tight_layout() 
plt.show() 