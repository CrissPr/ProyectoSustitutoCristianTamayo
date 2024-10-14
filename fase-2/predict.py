import argparse
import os
import pandas as pd
import pickle
from loguru import logger

# Default file paths
DEFAULT_INPUT_FILE = 'test.csv'
DEFAULT_PREDICTIONS_FILE = 'predictions.csv'
DEFAULT_MODEL_FILE = 'model.pkl'

parser = argparse.ArgumentParser()
parser.add_argument('--input_file', default=DEFAULT_INPUT_FILE, type=str, help='Path to the input data CSV file')
parser.add_argument('--predictions_file', default=DEFAULT_PREDICTIONS_FILE, type=str, help='Path to save predictions CSV file')
parser.add_argument('--model_file', default=DEFAULT_MODEL_FILE, type=str, help='Path to the trained model (pickle file)')

args = parser.parse_args()

input_file = args.input_file
predictions_file = args.predictions_file
model_file = args.model_file

if not os.path.isfile(model_file):
    logger.error(f"Model file '{model_file}' does not exist.")
    exit(-1)

if not os.path.isfile(input_file):
    logger.error(f"Input file '{input_file}' does not exist.")
    exit(-1)

logger.info("Loading input data...")
test_data = pd.read_csv(input_file)

# Data preprocessing
logger.info("Preprocessing data...")
test_data = test_data[['PassengerId', 'Age', 'Sex', 'Pclass']]
test_data['Age'].fillna(test_data['Age'].median(), inplace=True)
test_data = pd.get_dummies(test_data, columns=['Sex', 'Pclass'], drop_first=True)

# Ensure all expected columns are present
expected_cols = ['Age', 'Sex_male', 'Pclass_2', 'Pclass_3']
for col in expected_cols:
    if col not in test_data.columns:
        test_data[col] = 0

X_test = test_data.drop('PassengerId', axis=1)

logger.info("Loading the model...")
with open(model_file, 'rb') as f:
    model = pickle.load(f)

logger.info("Making predictions...")
predictions = model.predict(X_test)

logger.info(f"Saving predictions to '{predictions_file}'...")
output = pd.DataFrame({'PassengerId': test_data['PassengerId'], 'Survived': predictions})
output.to_csv(predictions_file, index=False)

logger.info("Prediction completed successfully.")

