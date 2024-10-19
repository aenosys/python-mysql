# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app

# Expose port 3000 to the outside world
EXPOSE 3000

# Run the app with Gunicorn in the container
CMD ["gunicorn", "-b", "0.0.0.0:3000", "app:app"]
