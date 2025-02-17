FROM python:3.10.8-slim-buster

# Update and install dependencies
RUN apt update && apt upgrade -y && apt install git -y

# Set working directory
WORKDIR /TheMovieProviderBot

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -U pip && pip3 install -U -r requirements.txt

# Copy bot files to container
COPY . .

# Ensure start.sh has execute permissions
RUN chmod +x start.sh

# Define the startup command
ENTRYPOINT ["bash", "start.sh"]
