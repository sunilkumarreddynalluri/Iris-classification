from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import json

app = Flask(__name__)

# Load pre-trained models
with open("KNN iris_predictions.pkl", "rb") as f:
    knn_model = pickle.load(f)

with open("Naive Bayes.pkl", "rb") as f:
    gnb_model = pickle.load(f)

# Iris dataset for metrics
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42
)


def get_results(model):
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    train_results = {
        "accuracy": round(accuracy_score(y_train, y_train_pred), 4),
        "confusion_matrix": confusion_matrix(y_train, y_train_pred).tolist(),
        "classification_report": classification_report(y_train, y_train_pred)
    }

    test_results = {
        "accuracy": round(accuracy_score(y_test, y_test_pred), 4),
        "confusion_matrix": confusion_matrix(y_test, y_test_pred).tolist(),
        "classification_report": classification_report(y_test, y_test_pred)
    }

    return train_results, test_results


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    try:
        features = np.array([
            float(data["sl"]),
            float(data["sw"]),
            float(data["pl"]),
            float(data["pw"])
        ]).reshape(1, -1)
    except ValueError:
        return jsonify({"error": "Invalid input. Please enter numeric values."})

    model_type = data.get("model")
    if model_type == "knn":
        model = knn_model
    elif model_type == "nb":
        model = gnb_model
    else:
        return jsonify({"error": "Invalid model type."})

    prediction_index = model.predict(features)[0]
    prediction_name = iris.target_names[prediction_index]

    train_results, test_results = get_results(model)

    return jsonify({
        "prediction": prediction_name,
        "train_results": train_results,
        "test_results": test_results
    })


if __name__ == "__main__":
    app.run(debug=True)