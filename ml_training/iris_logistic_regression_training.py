# Build and save the logistic regression model
# ============================================
import sys
print(sys.version)

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import pickle

# Load data
X, y = load_iris(return_X_y=True)

# Split training and test data
test_size = 0.33
seed = 7
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=seed)

# Create model
model = LogisticRegression(random_state=0, max_iter=100)

# fit model
clf = model.fit(X_train, y_train)

# Test classification
predictions = clf.predict(X_test[:, :])
clf.predict_proba(X_test[:, :])

score = clf.score(X_test, y_test)
print(score)

cm = metrics.confusion_matrix(y_test, predictions)
print(cm)

# Save model
filename =  "iris_regression_model.sav"
pickle.dump(model, open(filename, 'wb'))