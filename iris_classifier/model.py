from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

class IrisClassifier:
    def __init__(self):
        self.model = RandomForestClassifier()
        self._train()

    def _train(self):
        data = load_iris()
        X_train, _, y_train, _ = train_test_split(data.data, data.target, test_size=0.3, random_state=42)
        self.model.fit(X_train, y_train)

    def predict(self, features):
        return self.model.predict([features])[0]
