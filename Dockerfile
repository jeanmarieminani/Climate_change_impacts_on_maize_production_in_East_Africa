# Official Python runtime as a parent image
FROM python:3.9-slim

# Disable output buffering for real-time logs
ENV PYTHONUNBUFFERED=1

# Working directory
WORKDIR /app

# Python script into the container
COPY figure2.py .

# Data directory and copy CSV files
RUN mkdir -p /app/data
COPY east_africa_annual_temp_precip_1750_2023.csv /app/data/
COPY east_africa_maize_yields_tonne_ha_1961_2022.csv /app/data/
COPY World_clean_maize_data_1961_2022.csv /app/data/

# Grant full access to CSV files for the user
RUN chmod -R 777 /app/data

# Install dependencies
RUN pip install --no-cache-dir pandas matplotlib numpy

# Expose a volume for CSV files (to allow external access)
VOLUME ["/app/data"]

# Set default command to run the script
ENTRYPOINT ["python", "figure2.py"]
