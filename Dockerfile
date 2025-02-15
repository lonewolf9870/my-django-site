# Use official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV PORT=8080

# Expose the port for Cloud Run
EXPOSE 8080

# Start the server
CMD ["waitress-serve", "--listen=0.0.0.0:8080", "tech.wsgi:application"]
