# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY ServerGetAccepts.py /app

# Make port 8001 available to the world outside this container
EXPOSE 8001
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run ServerGetAccepts.py when the container launches
CMD ["python", "ServerGetAccepts.py"]
