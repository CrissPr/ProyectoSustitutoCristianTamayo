import subprocess
import pandas as pd

# Define file paths
train_data_file = 'train.csv'
test_data_file = 'test.csv'
model_file = 'model.pkl'
predictions_file = 'predictions.csv'

# Function to run a script with subprocess
def run_script(script, *args):
    command = ['python', script] + list(args)
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {script}: {result.stderr}")
    else:
        print(result.stdout)

# Train the model with --overwrite_model flag
print("Training the model...")
run_script('train.py', f'--data_file={train_data_file}', f'--model_file={model_file}', '--overwrite_model')

# Make predictions
print("\nMaking predictions...")
run_script('predict.py', f'--input_file={test_data_file}', f'--model_file={model_file}', f'--predictions_file={predictions_file}')

# Load and display predictions
print("\nLoading predictions...")
predictions = pd.read_csv(predictions_file)
print("\nPredictions:")
print(predictions.head())

