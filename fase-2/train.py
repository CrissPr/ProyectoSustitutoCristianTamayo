import argparse
import os
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from loguru import logger

# Default file paths
DEFAULT_DATA_FILE = 'train.csv'
DEFAULT_MODEL_FILE = 'model.pkl'

parser = argparse.ArgumentParser()
parser.add_argument('--data_file', default=DEFAULT_DATA_FILE, type=str, help='Path to the training data CSV file')
parser.add_argument('--model_file', default=DEFAULT_MODEL_FILE, type=str, help='Path to save the trained model (pickle file)')
parser.add_argument('--overwrite_model', action='store_true', help='Overwrite existing model file if it exists')

args = parser.parse_args()

data_file = args.data_file
model_file = args.model_file
overwrite = args.overwrite_model

if os.path.isfile(model_file) and not overwrite:
    logger.error(f"Model file '{model_file}' already exists. Use --overwrite_model to overwrite.")
    exit(-1)

if not os.path.isfile(data_file):
    logger.error(f"Data file '{data_file}' does not exist.")
    exit(-1)

logger.info("Loading training data...")
train_data = pd.read_csv(data_file)

# Data preprocessing
logger.info("Preprocessing data...")
train_data = train_data[['Survived', 'Age', 'Sex', 'Pclass']]
train_data['Age'].fillna(train_data['Age'].median(), inplace=True)
train_data = pd.get_dummies(train_data, columns=['Sex', 'Pclass'], drop_first=True)

X_train = train_data.drop('Survived', axis=1)
y_train = train_data['Survived']

logger.info("Training the model...")
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

logger.info(f"Saving model to '{model_file}'...")
with open(model_file, 'wb') as f:
    pickle.dump(model, f)

logger.info("Training completed successfully.")

