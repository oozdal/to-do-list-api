# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /TodoList2

# Copy the current directory contents into the container at /TodoList2
COPY . /TodoList2

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r TodoList2/requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV PORT=80

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]