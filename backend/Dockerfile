# Base image
FROM python:3.11.9

# Set working directory
WORKDIR /postgreSQLtest/backend

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Expose port
EXPOSE 8000

# Default command
# CMD ["sh", "-c", "python manage.py migrate && python create_superuser.py && python manage.py runserver 0.0.0.0:8000"]
# Default command to run migrations, create superuser, and start server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]