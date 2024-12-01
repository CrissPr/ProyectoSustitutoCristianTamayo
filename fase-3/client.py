import requests

# Endpoint for training the model
train_response = requests.post("http://localhost:5000/train")
print("Train Response:", train_response.json())

# Endpoint for prediction
predict_payload = {
    "input_file": "test.csv",
    "output_file": "predictions.csv",
}
predict_response = requests.post("http://localhost:5000/predict", json=predict_payload)
print("Predict Response:", predict_response.json())

