from flask import Flask, jsonify, request
from loguru import logger
import os
import subprocess

app = Flask(__name__)

MODEL_FILE = "model.pkl"
TRAIN_DATA = "train.csv"
TEST_DATA = "test.csv"
PREDICTIONS_FILE = "predictions.csv"


@app.route("/")
def hello_world():
    return jsonify({"message": "Welcome to the Titanic Model API"})


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    input_file = data.get("input_file", TEST_DATA)
    output_file = data.get("output_file", PREDICTIONS_FILE)

    if not os.path.exists(MODEL_FILE):
        return jsonify({"error": f"Model file '{MODEL_FILE}' not found"}), 400
    if not os.path.exists(input_file):
        return jsonify({"error": f"Input file '{input_file}' not found"}), 400

    logger.info("Starting prediction process...")
    result = subprocess.run(
        ["python", "predict.py", f"--input_file={input_file}", f"--model_file={MODEL_FILE}", f"--predictions_file={output_file}"],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        logger.error(f"Prediction failed: {result.stderr}")
        return jsonify({"error": result.stderr}), 500

    logger.info("Prediction completed successfully.")

    # Read the predictions from the output file and include them in the response
    try:
        with open(output_file, "r") as f:
            predictions = f.read().strip().split("\n")  # Assuming one prediction per line
        return jsonify({"message": "Predictions generated", "predictions": predictions})
    except Exception as e:
        logger.error(f"Failed to read predictions: {e}")
        return jsonify({"error": f"Failed to read predictions: {e}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


