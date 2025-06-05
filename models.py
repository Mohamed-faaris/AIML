from sklearn import datasets 
from sklearn.metrics import confusion_matrix, accuracy_score ,  mean_squared_error, r2_score, classification_report
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

from sklearn.naive_bayes import GaussianNB 
from sklearn.linear_model import LinearRegression 
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier 

iris = datasets.load_iris() 
X = iris.data 
y = iris.target 


# Step 2: Split data into train and test sets 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) 


# Step 3: Create and model 
model = DecisionTreeClassifier(max_depth= 2, random_state=42) 
model.fit(X_train, y_train) 


# Step 4: Predict and evaluate 
y_pred = model.predict(X_test) 
accuracy = accuracy_score(y_test, y_pred) 

print("Accuracy:", accuracy)


feature_names = iris.feature_names 
target_names = iris.target_names 
plot_tree(model, filled=True, feature_names=feature_names, class_names=target_names) 
plt.show()