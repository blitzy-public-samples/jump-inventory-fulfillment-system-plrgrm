#!/bin/bash

# Update system packages
echo "Updating system packages..."
sudo apt-get update
sudo apt-get upgrade -y

# Install required dependencies (Node.js, Python, etc.)
echo "Installing required dependencies..."
sudo apt-get install -y nodejs npm python3 python3-pip python3-venv postgresql

# Set up virtual environment for Python
echo "Setting up Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Install Node.js dependencies
echo "Installing Node.js dependencies..."
npm install

# Set up database
echo "Setting up database..."
sudo -u postgres psql -c "CREATE DATABASE myapp;"
sudo -u postgres psql -c "CREATE USER myappuser WITH PASSWORD 'mypassword';"
sudo -u postgres psql -c "ALTER ROLE myappuser SET client_encoding TO 'utf8';"
sudo -u postgres psql -c "ALTER ROLE myappuser SET default_transaction_isolation TO 'read committed';"
sudo -u postgres psql -c "ALTER ROLE myappuser SET timezone TO 'UTC';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE myapp TO myappuser;"

# Configure environment variables
echo "Configuring environment variables..."
cp .env.example .env
# HUMAN ASSISTANCE NEEDED
# TODO: Update .env file with appropriate values for your environment

# Run initial database migrations
echo "Running initial database migrations..."
python manage.py migrate

# Print setup completion message
echo "Development environment setup complete!"