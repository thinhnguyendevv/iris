# iris
# Iris Classifier

This is a simple Python package that uses a RandomForest classifier to classify iris flowers using the built-in scikit-learn iris dataset.

## Usage

```python
from iris_classifier import IrisClassifier

clf = IrisClassifier()
result = clf.predict([5.1, 3.5, 1.4, 0.2])
print("Predicted class:", result)
