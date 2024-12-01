# Use the base Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all project files to the container
COPY . /app

# Install required Python libraries
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask

# Expose the port for the Flask app
EXPOSE 5000

# Command to run the Flask app
CMD ["flask", "--app", "apirest", "run", "--host=0.0.0.0"]




