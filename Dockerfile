FROM python:3.12-slim

# Install distutils and other dependencies
RUN apt-get update && apt-get install -y python3-distutils build-essential && apt-get clean

# Set the working directory
WORKDIR /scripts

# Copy requirements file
COPY requirements.txt .

# Install numpy first
RUN pip install --no-cache-dir numpy==1.24.4

# Install other dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose port and define entrypoint
EXPOSE 5000
CMD ["python", "app.py"]
