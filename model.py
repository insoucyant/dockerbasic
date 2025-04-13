# import pandas as pd
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
# Load the Iris Dataset
iris = load_iris()
X,y = iris.data, iris.target
# Train the Random Forest Classifier
model = RandomForestClassifier()
model.fit(X,y)
# Save the trained model 
joblib.dump(model, 'model.joblib')