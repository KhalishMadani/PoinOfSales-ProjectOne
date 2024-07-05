# Use an official Python runtime as a parent image
FROM python:3.12.0-slim-bullseye

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PORT 8000

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose the port the app runs on
EXPOSE ${PORT}

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
