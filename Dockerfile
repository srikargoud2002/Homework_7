# Use Python 3.9 as the base image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Set environment variables (defaults that can be overridden)
ENV QR_DATA_URL='https://github.com/srikargoud2002'
ENV QR_CODE_DIR='qr_codes'
ENV QR_CODE_FILENAME='qrcode.png'
ENV FILL_COLOR='black'
ENV BACK_COLOR='white'

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script
COPY app.py .

# Create a volume for the QR codes directory
VOLUME /app/qr_codes

# Command to run when container starts
ENTRYPOINT ["python", "app.py"]