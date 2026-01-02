import json
import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))
with open("symptom_index.json", "r") as f:
    symptom_cols = json.load(f)


def encode_input(data_dict):
    # data_dict: {"fever":1, "cough":0, ...}
    vec = [int(data_dict.get(col, 0)) for col in symptom_cols]
    return [vec]


@app.route("/predict", methods=["POST"])
def predict():
    payload = request.json
    X_in = encode_input(payload)
    pred = model.predict(X_in)[0]
    return jsonify({"Predicted Disease": pred})


if __name__ == "__main__":
    app.run(debug=True)
