from sklearn import datasets
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
iris = datasets.load_iris()
X = iris.data
Y = iris.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=1/3, random_state=42)

model = GaussianNB()
model.fit(X_train, Y_train)

model_predictions = model.predict(X_test)

print("\nPredictions:", model_predictions)
print("\nActual labels:", Y_test)

accuracyScore = accuracy_score(Y_test, model_predictions)
print("\nAccuracy Score:", accuracyScore)

cm = confusion_matrix(Y_test, model_predictions)
print("\nConfusion Matrix:\n", cm)





