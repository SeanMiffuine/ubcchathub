FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file and install dependencies
COPY mysite/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port your Django app runs on (e.g., 8000)
EXPOSE 8000
EXPOSE 8001

# Start the Django development server
CMD ["python", "mysite/manage.py", "runserver"]